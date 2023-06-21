import pytest
# about keyword arguments


def method_with_kwargs(a=None, b=None):
    return f"got {a} and {b}"


def method_with_kwargs_as_hash(**kwargs):
    a = kwargs['a']
    b = kwargs['b']
    return f"got {a} and {b}"


def method_with_kwargs_just_delegates(**kwargs):
    return method_with_kwargs(**kwargs)


def method_with_kwargs_just_delegates_to_hash(**kwargs):
    return method_with_kwargs_as_hash(**kwargs)


variants = [method_with_kwargs,
            method_with_kwargs_as_hash,
            method_with_kwargs_just_delegates,
            method_with_kwargs_just_delegates_to_hash]


@pytest.mark.parametrize('method_variant', variants)
def test_call_method_with_kwargs(method_variant):
    assert 'got foo and bar' == method_variant(a='foo', b='bar')


@pytest.mark.parametrize('method_variant', variants)
def test_call_method_with_positional_args(method_variant):
    assert 'got foo and bar' == method_with_kwargs('foo', 'bar')


@pytest.mark.parametrize('method_variant', variants)
def test_call_method_with_dict(method_variant):
    a_dict = {'a': 'foo', 'b': 'bar'}
    assert 'got foo and bar' == method_with_kwargs(**a_dict)
