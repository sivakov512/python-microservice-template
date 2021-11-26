{%- set grpc_support = cookiecutter.grpc_servicer | trim != "" -%}

{%- if grpc_support %}
{%- set import_path, import_module, servicer_name = cookiecutter.grpc_servicer.rsplit('.', 2) %}
{%- set import_module = import_module + "_pb2_grpc" %}
{%- set servicer_name = servicer_name + "Servicer" %}
{%- endif -%}

{%- if grpc_support -%}
from dataclasses import dataclass

{% endif -%}
from asyncpg_engine import Engine
{%- if grpc_support %}

from {{ import_path }} import {{ import_module }}
{%- endif %}

__all__ = [{%- if grpc_support %}"Handler", {% endif -%}"RequiredProcedures"]


class RequiredProcedures:
    def __init__(self, db: Engine):
        pass
{%- if grpc_support %}


@dataclass
class Handler({{ import_module }}.{{ servicer_name }}):
    procedures: RequiredProcedures
{%- endif %}
