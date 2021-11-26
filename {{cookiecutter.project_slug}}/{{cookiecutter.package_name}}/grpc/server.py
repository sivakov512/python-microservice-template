{%- set grpc_support = cookiecutter.grpc_servicer | trim != "" -%}

{%- if grpc_support %}
{%- set import_path, import_module, servicer_name = cookiecutter.grpc_servicer.rsplit('.', 2) %}
{%- set import_module = import_module + "_pb2_grpc" %}
{%- set servicer_name = servicer_name + "Servicer" %}
{%- endif -%}

import logging

import grpc.aio
from asyncpg_engine import Engine
{%- if grpc_support %}

from {{ import_path }} import {{ import_module }}
{%- endif %}

from .handler import {% if grpc_support -%}Handler, {% endif -%}RequiredProcedures

__all__ = ["run"]


async def run(postgres_url: str, port: int) -> None:
    listen_addr = f"[::]:{port}"

    engine = await Engine.create(postgres_url)
    procedures = RequiredProcedures(engine)
    server = grpc.aio.server()
    {%- if grpc_support %}

    {{ import_module }}.add_{{ servicer_name }}_to_server(Handler(procedures), server)
    {% else %}

    # TODO: add your servicer implementation to server here
    {% endif -%}
    server.add_insecure_port(listen_addr)

    logging.info("Starting grpc server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()
