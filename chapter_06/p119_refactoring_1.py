import pytest

# ############# Page 119 ##############
# The way to refactor:
# Start with empty abstraction class!

# This class is now empty.
# All code has been moved to RoadBike.


class Bicycle:
    def __init__(self, **kwargs):
        pass

    def spares(self):
        return {}


class RoadBike(Bicycle):
    def __init__(self, **kwargs):
        self.size = kwargs.get('size')
        self.tape_color = kwargs.get('tape_color')

    def spares(self):
        return {
            'chain': '10-speed',
            'tire_size': '23',
            'tape_color': self.tape_color
        }


class MountainBike(Bicycle):
    def __init__(self, **kwargs):
        self.front_shock = kwargs.get('front_shock')
        self.rear_shock = kwargs.get('rear_shock')
        # super().__init__(**kwargs)

    def spares(self):
        spares = super().spares().copy()
        spares.update({'rear_shock': self.rear_shock})
        return spares

############## Page 120 ##############

# => now the abstractions need to be identified and
# moved up from RoadBike to Bicycle


def test_spares():
    bike = RoadBike(size='M', tape_color='red')
    assert bike.size == 'M'
    assert bike.spares() == {'tire_size': '23',
                             'chain': '10-speed',
                             'tape_color': 'red'}


mountain_bike = MountainBike(
    size='S',
    front_shock='Manitou',
    rear_shock='Fox'
)


@pytest.mark.xfail(reason="no super init")
def test_spares_mountain_bike():
    assert mountain_bike.spares() == {
        'chain': '10-speed', 'tire_size': '23', 'tape_color': None, 'rear_shock': 'Fox'}


@pytest.mark.xfail(reason="no super init")
def test_size_mountain_bike():
    assert mountain_bike.size == 'S'
