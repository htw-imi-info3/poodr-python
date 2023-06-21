from typing import List
import functools
import collections.abc as abc


class Bicycle:

    def __init__(self, **args):
        self.size = args.get('size')
        self.parts = args.get('parts')

    def spares(self):
        return self.parts.spares()

    def __repr__(self):
        return f"Bicycle(size={self.size}, parts={self.parts})"


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


class Parts(abc.Sequence):
    def __init__(self, parts=None):
        self.parts = parts or []

    def spares(self):
        return Parts([part for part in self.parts if part.needs_spare])

    def __getitem__(self, index):
        return self.parts.__getitem__(index)
    
    def __len__(self):
        return len(self.parts)

    def __add__(self, other):
        return Parts(self.parts + list(other))

    def __repr__(self):
        return f"Parts(parts={self.parts})"


ROAD_CONFIG = [
    ['chain', '10-speed'],
    ['tire_size', '23'],
    ['tape_color', 'red']
]

MOUNTAIN_CONFIG = [
    ['chain', '10-speed'],
    ['tire_size', '2.1'],
    ['front_shock', 'Manitou', False],
    ['rear_shock', 'Fox']
]


class PartsFactory:
    @staticmethod
    def build(config: List[List[str]],
              part_class=Part,
              parts_class=Parts) -> Parts:
        parts = [part_class(name=part[0],
                 description=part[1],
                 needs_spare=part[2] if len(part) > 2 else True)
                 for part in config]
        return parts_class(parts)


road_parts = PartsFactory.build(ROAD_CONFIG)
mountain_parts = PartsFactory.build(MOUNTAIN_CONFIG)

road_bike = Bicycle(size='L', 
                    parts=PartsFactory.build(ROAD_CONFIG))
mountain_bike = Bicycle(size='M', 
                        parts=PartsFactory.build(MOUNTAIN_CONFIG))



def test_road_bike():
    assert road_bike.spares() == {}
 
def test_mountain_bike():
    assert mountain_bike.spares() == {}
       
