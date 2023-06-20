class Bicycle:
    def __init__(self, **kwargs):
        self.size = kwargs['size']
        self.tape_color = kwargs['tape_color']

    def spares(self):
        return {
            'chain': '10-speed',
            'tire_size': '23',
            'tape_color': self.tape_color
        }


class MountainBike(Bicycle):
    def spares(self):
        super_spares = super().spares()
        super_spares['rear_shock'] = self.rear_shock
        return super_spares


def test_spares():
    bike = Bicycle(size='M', tape_color='red')
    assert bike.size == 'M'
    assert bike.spares() == {'tire_size': '23',
                             'chain': '10-speed',
                             'tape_color': 'red'}


def test_spares_mountain_bike():
    mountain_bike = MountainBike(
        size='S',
        front_shock='Manitou',
        rear_shock='Fox'
    )
    assert mountain_bike.size == 'S'

    assert mountain_bike.spares() == {
        'chain': '10-speed', 'tire_size': '23', 'tape_color': None, 'rear_shock': 'Fox'}
