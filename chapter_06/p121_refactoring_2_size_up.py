class Bicycle:
    def __init__(self, **kwargs):
        self.size = kwargs.get('size')


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
        self.front_shock = kwargs.get('front_shock')
        self.rear_shock = kwargs.get('rear_shock')
        super().__init__(**kwargs)

    def spares(self):
        return super().spares().copy().update({'rear_shock': self.rear_shock})


road_bike = RoadBike(
    size='M',
    tape_color='red'
)
print(road_bike.size)  # => "M"

mountain_bike = MountainBike(
    size='S',
    front_shock='Manitou',
    rear_shock='Fox'
)
print(mountain_bike.size)  # => "S"
