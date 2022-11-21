import os

import pytest

from defineif import DefineIf


class BasicClassTrue(DefineIf):
    @DefineIf(True)
    def f(self):
        return True


class BasicClassTrueMethod(DefineIf):
    @DefineIf(True)
    def method(self):
        return True


class BasicClassFalse(DefineIf):
    @DefineIf(False)
    def f(self):
        return False


def test_basic_class_true():
    assert BasicClassTrue().f() is True
    assert BasicClassTrueMethod().method() is True


def test_basic_class_false():
    with pytest.raises(AttributeError):
        BasicClassFalse().f()


def test_basic_class_true_multi_call():
    assert BasicClassTrue().f() is True
    assert BasicClassTrue().f() is True
    assert BasicClassTrue().f() is True
    assert BasicClassTrue().f() is True
    assert BasicClassTrueMethod().method() is True
    assert BasicClassTrueMethod().method() is True


def test_basic_class_false_true_same_time():
    with pytest.raises(AttributeError):
        BasicClassFalse().f()

    assert BasicClassTrue().f() is True
    assert BasicClassTrueMethod().method() is True


def test_main():
    class BasicClassTrue(DefineIf):
        @DefineIf(True)
        def f(self):
            return True

        @DefineIf(False)
        def f(self):
            return False

    assert BasicClassTrue().f() is True


from defineif import DefineIf


class Klass(DefineIf):
    @staticmethod
    @DefineIf(os.name == "nt")
    def get_platform():
        return "Windows"

    @staticmethod
    @DefineIf(os.name == "posix")
    def get_platform():
        return "Linux"


def test_get_platform():
    platform = Klass.get_platform()
    assert platform == ("Windows" if os.name == "nt" else "Linux")
