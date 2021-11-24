#!/usr/bin/env python
import asyncio
import logging

import click

from {{ cookiecutter.package_name }} import grpc


@click.command()
@click.option("--port", default=8080, type=int, help="Port to bind to")
@click.option("--postgres-url", envvar="POSTGRES_URL", type=str, help="Postgres url to connect to")
def cli(port: int, postgres_url: str) -> None:
    logging.basicConfig(level=logging.INFO)
    asyncio.run(grpc.run_server(postgres_url, port))


if __name__ == "__main__":
    cli()
