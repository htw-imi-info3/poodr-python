import functools
import collections.abc as abc


class Bicycle:

    def __init__(self, **args):
        self.size = args.get('size')
        self.parts = args.get('parts')

    def spares(self):
        return self.parts.spares()


def is_iterable(something):
    """
    see https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable

    Returns:
        boolean: True if object implements iter()
    """
    try:
        iter(something)
    except TypeError:
        return False
    return True


class Parts(abc.Sequence):
    """ a list of Part elements
    in the Ruby version, Parts behaves like a list(array)
    by delegating relevant methods to the wrapped list (self.parts)
    
    The Pythonic way is more explicit, 
    https://docs.python.org/3.11/reference/datamodel.html#emulating-container-types
    contains guidance on how to implement own container types,
    using provided Abstract Base Classes:
    https://docs.python.org/3.11/library/collections.abc.html#collections-abstract-base-classes
    
    """
    def __init__(self, parts=None):
        self.parts = parts or []

    def spares(self):
        return Parts([part for part in self.parts if part.needs_spare])

    def __getitem__(self, index):
        return self.parts.__getitem__(index)
    
    def __len__(self):
        return len(self.parts)

    def __add__(self, other):
        """implements the + operator

        unlike in the Ruby original, all unknown methods
        are delegated to the wrapped list.
        While this would be possible in python,
        more explicit ways are more pythonic.
        """
        if is_iterable(other):
            return Parts(list(self.parts) + list(other))
        else:
            raise TypeError('other object needs to be iterable')

    def __repr__(self):
        return f"Parts(parts={self.parts})"


# see https://docs.python.org/3/library/functools.html
@functools.total_ordering
class Part:
    def __init__(self, **args):
        self.name = args.get('name')
        self.description = args.get('description')
        self.needs_spare = args.get('needs_spare', True)

    def needs_spare(self):
        return self.needs_spare

    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        return self.name == other.name


# Tests


chain = Part(name='chain', description='10-speed')
road_tire = Part(name='tire_size', description='23')
tape = Part(name='tape_color', description='red')
mountain_tire = Part(name='tire_size', description='2.1')
rear_shock = Part(name='rear_shock', description='Fox')
front_shock = Part(
    name='front_shock',
    description='Manitou',
    needs_spare=False
)


def test_parts_has_len():
    p1 = Parts([chain, mountain_tire, front_shock, rear_shock])
    assert len(p1) == 4
    p2 = Parts([chain, road_tire, tape])
    assert len(p2) == 3


def test_parts_can_be_combined():
    p1 = Parts([chain, mountain_tire, front_shock, rear_shock])
    p2 = Parts([chain, road_tire, tape])
    p3 = p1 + p2
    assert len(p3) == 7


mountain_bike = Bicycle(
    size='L',
    parts=Parts([chain, mountain_tire, front_shock, rear_shock])
)


def test_mountain_bike():
    assert len(mountain_bike.parts) == 4
    assert len(mountain_bike.spares()) == 3


road_bike = Bicycle(size='M',
                    parts=Parts([chain, road_tire, tape]))


def test_road_bike():
    assert len(road_bike.parts) == 3
    assert len(road_bike.spares()) == 3

