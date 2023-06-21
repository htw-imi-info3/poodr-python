import pytest


class Bicycle:

    def __init__(self, **args):
        self.size = args.get('size')
        self.parts = args.get('parts')

    def spares(self):
        return self.parts.spares()


class Parts:
    def __init__(self, **args):
        self.chain = args.get('chain') or self.default_chain()
        self.tire_size = args.get('tire_size') or self.default_tire_size()
        self.post_initialize(**args)

    def spares(self):
        spares = {
            'tire_size': self.tire_size,
            'chain': self.chain
        }
        spares.update(self.local_spares())
        return spares

    def default_tire_size(self):
        raise NotImplementedError(
            'Parts subclasses must implement default_tire_size')

    def post_initialize(self, **args):
        pass

    def local_spares(self):
        return {}

    def default_chain(self):
        return '10-speed'


class RoadBikeParts(Parts):
    def post_initialize(self, **args):
        self.tape_color = args.get('tape_color')

    def local_spares(self):
        return {'tape_color': self.tape_color}

    def default_tire_size(self):
        return '23'


class MountainBikeParts(Parts):
    def post_initialize(self, **args):
        self.front_shock = args.get('front_shock')
        self.rear_shock = args.get('rear_shock')

    def local_spares(self):
        return {'rear_shock': self.rear_shock}

    def default_tire_size(self):
        return '2.1'


# Testing the code


road_bike = Bicycle(size='L',
                    parts=RoadBikeParts(tape_color='red'))


def test_road_bike():
    assert road_bike.size == 'L'
    assert road_bike.spares() == {'tire_size': '23',
                                  'chain': '10-speed',
                                  'tape_color': 'red'}


mountain_bike = Bicycle(size='L',
                        parts=MountainBikeParts(rear_shock='Fox'))


def test_mountain_bike():
    assert mountain_bike.size == 'L'
    assert mountain_bike.spares() == {'tire_size': '2.1',
                                      'chain': '10-speed',
                                      'rear_shock': 'Fox'}

