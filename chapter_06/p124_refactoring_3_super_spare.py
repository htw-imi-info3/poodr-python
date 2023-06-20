class Bicycle:
    def __init__(self, args={}):
        self.size = args.get('size')
        self.chain = args.get('chain')
        self.tire_size = args.get('tire_size')

class RoadBike(Bicycle):
    def spares(self):
        return {
            'chain': '10-speed',
            'tire_size': '23',
            'tape_color': self.tape_color
        }

class MountainBike(Bicycle):
    def __init__(self, args={}):
        self.rear_shock = args.get('rear_shock')
        super().__init__(args)

    def spares(self):
        return super().spares().update({'rear_shock': self.rear_shock})
