import functools

class Bicycle:

    def __init__(self, **args):
        self.size = args.get('size')
        self.parts = args.get('parts')

    def spares(self):
        return self.parts.spares()


class Parts:
    def __init__(self, parts=None):
        self.parts = parts or []

    def spares(self):
        return Parts([part for part in self.parts if part.needs_spare()])

    def __len__(self):
        return len(self.parts)

    def __iter__(self):
        return iter(self.parts)

    def __add__(self, other):
        if isinstance(other, Iterable):
            return Parts(list(self.parts) + list(other))
        else:
            return NotImplemented

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

Part = namedtuple('Part', ['name', 'description', 'needs_spare'])

# Duplicated code removed for brevity

mountain_bike = Bicycle({
    'size': 'L',
    'parts': Parts([chain, mountain_tire, front_shock, rear_shock])
})
print(mountain_bike.spares().size)  # -> 3
print(len(mountain_bike.parts))     # -> 4

road_bike = Bicycle({
    'size': 'M',
    'parts': Parts([chain, road_tire, tape])
})
print(road_bike.spares().size)      # -> 3
print(len(road_bike.parts))         # -> 4

class Parts:
    def_delegators = forwardable.def_delegators

    def __init__(self, parts):
        self.parts = parts

print(mountain_bike.parts + road_bike.parts)
# -> TypeError: unsupported operand type(s) for +: 'Parts' and 'Parts'
