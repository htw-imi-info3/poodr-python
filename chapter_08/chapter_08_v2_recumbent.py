from chapter_08.chapter_08_v2 import Parts, Part, Bicycle

# add recumbent_bike - working:


class RecumbentBikeParts(Parts):

    def post_initialize(self, **args):
        self.flag = args.get('flag')

    def default_tire_size(self):
        return '28'

    def local_spares(self):
        return {'flag': self.flag}


chain = Part(name='chain', description='10-speed')
tire = Part(name='tire_size', description='28')

flag = Part(
    name='flag',
    description='Rainbow',
    needs_spare=True
)


def test_recumbent_bike_2():
    recumbent_bike = Bicycle(
        size='L',
        parts=RecumbentBikeParts([flag, chain, tire]))

    assert str(recumbent_bike.spares(
    )) == 'Parts(parts=[Part(name=flag, description=Rainbow, needs_spare=True), Part(name=chain, description=10-speed, needs_spare=True), Part(name=tire_size, description=28, needs_spare=True)])'
