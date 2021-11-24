import logging

import grpc.aio
from asyncpg_engine import Engine

from .handler import RequiredProcedures

__all__ = ["run"]


async def run(postgres_url: str, port: int) -> None:
    listen_addr = f"[::]:{port}"

    engine = await Engine.create(postgres_url)
    procedures = RequiredProcedures(engine)
    server = grpc.aio.server()

    server.add_insecure_port(listen_addr)

    logging.info("Starting grpc server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()
