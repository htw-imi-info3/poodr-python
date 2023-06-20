class Bicycle:
    def __init__(self, size, tape_color):
        self.size = size
        self.tape_color = tape_color

    def spares(self):
        return {
            'chain': '10-speed',
            'tire_size': '23',
            'tape_color': self.tape_color
        }


def test_spares():
    bike = Bicycle(size='M', tape_color='red')
    assert bike.size == 'M'
    assert bike.spares() == {'tire_size': '23',
                             'chain': '10-speed',
                             'tape_color': 'red'}
