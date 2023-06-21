from chapter_08.chapter_08_v3 import Bicycle, PartsFactory

RECUMBENT_CONFIG = [
    ['chain', '9-speed'],
    ['tire_size', '28'],
    ['flag', 'tall and orange']
]

recumbent_bike = Bicycle(size='S', parts=PartsFactory.build(RECUMBENT_CONFIG))


def test_recumbent_bike():
    assert recumbent_bike.size == 'S'


def test_recumbent_bike_spares():
    assert str(recumbent_bike.spares()) == 'Parts(parts=[' +\
        'Part(name=chain,description=9-speed,needs_spare=True), ' +\
        'Part(name=tire_size,description=28,needs_spare=True), ' +\
        'Part(name=flag,description=tall and orange,needs_spare=True)])'
