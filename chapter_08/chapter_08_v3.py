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


class Part:
    def __init__(self, name=None, description=None, needs_spare=True):
        self.name = name
        self.description = description
        self.needs_spare = needs_spare

    def __repr__(self):
        return f"Part(name={self.name}, description={self.description}, needs_spare={self.needs_spare})"


class Parts:
    def __init__(self, parts=None):
        self.parts = parts or []

    def spares(self):
        return Parts([part for part in self.parts if part.needs_spare])

    def __len__(self):
        return len(self.parts)

    def __iter__(self):
        return iter(self.parts)

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
    def build(config: List[List[str]], part_class=Part, parts_class=Parts) -> Parts:
        parts = [part_class(name=part[0], description=part[1], needs_spare=part[2] if len(part) > 2 else True)
                 for part in config]
        return parts_class(parts)


road_parts = PartsFactory.build(ROAD_CONFIG)
mountain_parts = PartsFactory.build(MOUNTAIN_CONFIG)

road_bike = Bicycle(size='L', parts=PartsFactory.build(ROAD_CONFIG))
print(road_bike.spares())  # -> Parts(parts=[Part(name=chain, description=10-speed, needs_spare=True), ...])

mountain_bike = Bicycle(size='L', parts=PartsFactory.build(MOUNTAIN_CONFIG))
print(mountain_bike.spares())  # -> Parts(parts=[Part(name=chain, description=10-speed, needs_spare=True), ...])
