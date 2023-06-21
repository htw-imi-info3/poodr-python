import pytest
from chapter_08.chapter_08_v1 import Parts, Bicycle

# add recumbent_bike - attempt #1: - forgetting to override abstract method:

class RecumbentBikeParts1(Parts):
    def post_initialize(self, **args):
        self.flag = args.get('flag')


def test_recumbent_bike_not_working():
    with pytest.raises(NotImplementedError, match='must implement default_tire_size'):
        recumbent_bike = Bicycle(size='L',
                                 parts=RecumbentBikeParts1(flag='Rainbow'))

# add recumbent_bike - attempt #2: - forgetting to override local_spares:


class RecumbentBikeParts2(Parts):
    def post_initialize(self, **args):
        self.flag = args.get('flag')

    def default_tire_size(self):
        return '28'


def test_recumbent_bike_2():
    recumbent_bike = Bicycle(size='L',
                             parts=RecumbentBikeParts2(flag='Rainbow'))

    assert recumbent_bike.spares() == {'tire_size': '28', 'chain': '10-speed'}


# add recumbent_bike - working:

class RecumbentBikeParts3(Parts):

    def post_initialize(self, **args):
        self.flag = args.get('flag')

    def default_tire_size(self):
        return '28'

    def local_spares(self):
        return {'flag': self.flag}


def test_recumbent_bike_2():
    recumbent_bike = Bicycle(size='L',
                             parts=RecumbentBikeParts3(flag='Rainbow'))

    assert recumbent_bike.spares() == {
        'chain': '10-speed',
        'flag': 'Rainbow',
        'tire_size': '28'}
