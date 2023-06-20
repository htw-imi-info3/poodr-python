import pytest

class Bicycle:
    def __init__(self, **kwargs):
        self.size = kwargs.get('size')
        self.chain = kwargs.get('chain', self.default_chain())
        self.tire_size = kwargs.get('tire_size', self.default_tire_size())
    
    def default_chain(self):
        return '10-speed'
    
    def spares(self):
        return {
            'chain': self.chain,
            'tire_size': self.tire_size
        }


class RoadBike(Bicycle):

    def __init__(self, **kwargs):
        self.tape_color = kwargs.get('tape_color')
        super().__init__(**kwargs)
        
    def default_tire_size(self):
        return '23'
    
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
        
    def default_tire_size(self):
        return '2.1'
    
    def spares(self):
        spares = super().spares()
        spares.update({'rear_shock': self.rear_shock})
        return spares
    

    

    

# Testing the code

road_bike = RoadBike(size='M', tape_color='red')
 

def test_spares_road_bike():
    road_bike = RoadBike(size='M', tape_color='red')
    assert road_bike.size == 'M'
    assert road_bike.spares() == {'tire_size': '23',
                             'chain': '10-speed',
                             'tape_color': 'red'}


def test_defaults_road_bike():
    assert road_bike.tire_size == '23'
    assert road_bike.chain ==  '10-speed'


mountain_bike = MountainBike(
    size='S',
    front_shock='Manitou',
    rear_shock='Fox'
)


@pytest.mark.xfail(False, reason="only size fixed in this step")
def test_spares_mountain_bike():
    assert mountain_bike.spares() == {
        'chain': '10-speed',
        'tire_size': '2.1', 
        'rear_shock': 'Fox'}


def test_size_mountain_bike():
    assert mountain_bike.size == 'S'

  
def test_defaults_mountain_bike():
    assert mountain_bike.tire_size == '2.1'
    assert mountain_bike.chain == '10-speed'
