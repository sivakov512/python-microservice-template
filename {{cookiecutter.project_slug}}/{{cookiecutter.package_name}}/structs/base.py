import abc
import typing as t

__all__ = ["ProtoConvertable"]


class ProtoConvertable:
    @abc.abstractclassmethod
    def from_proto(cls, message: t.Any) -> "ProtoConvertable":
        pass

    @abc.abstractmethod
    def to_proto(self) -> t.Any:
        pass
