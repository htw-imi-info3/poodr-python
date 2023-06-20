class Bicycle:
    def __init__(self, style, size, tape_color, front_shock=None,
                 rear_shock=None):
        self.style = style
        self.size = size
        self.tape_color = tape_color
        self.front_shock = front_shock
        self.rear_shock = rear_shock

    def spares(self):
        if self.style == 'road':
            return {
                'chain': '10-speed',
                'tire_size': '23',       # millimeters
                'tape_color': self.tape_color
            }
        else:
            return {
                'chain': '10-speed',
                'tire_size': '2.1',      # inches
                'rear_shock': self.rear_shock
            }


def test_spares():
    bike = Bicycle(style='road', size='M', tape_color='red')
    assert bike.size == 'M'
    assert bike.spares() == {'tire_size': '23',
                             'chain': '10-speed',
                             'tape_color': 'red'}


def test_spares_mountain_bike():
    bike = Bicycle(style='mountain', size='S', tape_color=None,
                   front_shock='Manitou', rear_shock='Fox')
    assert bike.size == 'S'
    assert bike.spares() == {'chain': '10-speed',
                             'tire_size': '2.1',
                             'rear_shock': 'Fox'}
