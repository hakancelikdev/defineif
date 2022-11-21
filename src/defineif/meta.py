import inspect
import typing

__all__ = ("Meta", "StoreNamespace")


FuncT = typing.Callable[[typing.Any], typing.Any]  # unexport: not-public


class NotSet:  # unexport: not-public
    ...


class StoreNamespace(dict):
    test: typing.List[bool] = []  # TODO: rename

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().__setitem__("define_if", self.define_if)

    def __setitem__(self, key: str, value: typing.Any):
        if inspect.isfunction(value):
            if self.test:
                if self.test.pop() is True:
                    super().__setitem__(key, value)
            else:
                super().__setitem__(key, value)
        else:
            super().__setitem__(key, value)

    @classmethod
    def define_if(cls, condition: bool) -> typing.Callable[[typing.Callable], FuncT]:
        def wrapper(func: FuncT) -> FuncT:
            cls.test.append(condition)
            return func

        return wrapper


class Meta(type):
    if typing.TYPE_CHECKING:

        @classmethod
        def define_if(mcs, condition: bool) -> typing.Callable[[typing.Callable], FuncT]:
            ...

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs) -> typing.Union["StoreNamespace", dict]:  # type: ignore[override]  # noqa: E501
        return StoreNamespace()

    def __call__(cls, condition: typing.Union[bool, typing.Type[NotSet], None] = NotSet):
        if condition is NotSet:
            return super().__call__()
        else:
            assert isinstance(condition, bool)
            return cls.define_if(condition)
