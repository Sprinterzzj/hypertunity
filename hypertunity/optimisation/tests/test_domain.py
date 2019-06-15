# -*- coding: utf-8 -*-

import pytest

from collections import namedtuple

from ..domain import Domain


def test_valid():
    with pytest.raises(TypeError):
        Domain({{"b": lambda x: x}, [0, 0.1]})
    with pytest.raises(ValueError):
        Domain({1: {"b": [2, 3]}, "c": [0, 0.1]})
    with pytest.raises(ValueError):
        Domain({"a": {"b": {1, 2, 3, 4}}, "c": [0, 0.1]})
    with pytest.raises(ValueError):
        Domain({"a": {"b": lambda x: x}, "c": [0, 0.1]})
    with pytest.raises(ValueError):
        # this one should fail from the ast.literal_eval parsing
        Domain('{"a": {"b": lambda x: x}, "c": [0, 0.1]}')
    Domain({"a": {"b": [0, 1]}, "c": [0, 0.1]})
    Domain('{"a": {"b": [0, 1]}, "c": [0, 0.1]}')


def test_eq():
    d1 = Domain({"a": {"b": [2, 3]}, "c": [0, 0.1]})
    d2 = Domain({"a": {"b": [2, 3]}, "c": [0, 0.1]})
    assert d1 == d2


def test_serialisation():
    domain = Domain({"a": [1, 2], "b": {"c": (1, 2, 3), "d": ("o1", "o2")}})
    serialised = domain.serialise()
    deserialised = Domain.deserialise(serialised)
    assert deserialised == domain


def test_conversions():
    dict_domain = {"a": {"b": [2, 3]}, "c": [0, 0.1]}
    domain = Domain(dict_domain)
    assert domain.as_dict() == dict_domain


def test_as_namedtuple():
    domain = Domain({"a": {"b": (2, 3, 4)}, "c": [0, 0.1]})
    nt = domain.as_namedtuple()
    assert nt.a == namedtuple("_", "b")((2, 3, 4))
    assert nt.a.b == (2, 3, 4)
    assert nt.c == [0, 0.1]
