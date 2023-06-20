import pytest


class Bicycle:
    def __init__(self, **kwargs):
        self.size = kwargs.get('size')
        self.chain = kwargs.get('chain', '10-speed')
        self.tire_size = kwargs.get('tire_size', '23')

    def spares(self):
        return {
            'chain': self.chain,
            'tire_size': self.tire_size
        }


class RoadBike(Bicycle):
    def __init__(self, **kwargs):
        self.tape_color = kwargs.get('tape_color')
        super().__init__(**kwargs)

    def spares(self):
        return {
            'chain': '10-speed',
            'tire_size': '23',
            'tape_color': self.tape_color
        }


class MountainBike(Bicycle):
    def __init__(self, **kwargs):
        self.rear_shock = kwargs.get('rear_shock')
        self.rear_shock = kwargs.get('rear_shock')
        super().__init__(**kwargs)

    def spares(self):
        spares = super().spares()
        spares.update({'rear_shock': self.rear_shock})
        return spares


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


@pytest.mark.xfail(False, reason="only size fixed in this step")
def test_spares_mountain_bike():
    assert mountain_bike.spares() == {
        'chain': '10-speed',
        'tire_size': '23', 
        'rear_shock': 'Fox'}


def test_size_mountain_bike():
    assert mountain_bike.size == 'S'
