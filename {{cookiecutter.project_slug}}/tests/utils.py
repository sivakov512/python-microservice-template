import typing as t
from dataclasses import dataclass
from unittest import mock

import grpc.aio

__all__ = ["Any", "servicer_context"]


@dataclass
class Any:
    typeof: t.Any

    def __eq__(self, another: t.Any) -> bool:
        return isinstance(another, self.typeof)


def servicer_context() -> t.Any:
    return mock.create_autospec(spec=grpc.aio.ServicerContext)
