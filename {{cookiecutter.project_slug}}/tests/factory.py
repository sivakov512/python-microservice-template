from dataclasses import dataclass

import pytest
from asyncpg import Connection


@dataclass
class Factory:
    __slots__ = ("con",)

    con: Connection


@pytest.fixture()
def factory(con: Connection) -> Factory:
    return Factory(con)
