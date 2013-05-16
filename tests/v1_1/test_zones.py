from novaclient import exceptions
from novaclient.v1_1 import zones
from tests import utils
from tests.v1_1 import fakes


cs = fakes.FakeClient()


class ZonesTest(utils.TestCase):

    def test_zones(self):
        zl = cs.zones.add('zone1')
        self.assertEqual(1, len(zl))
        zl = cs.zones.add('zone1', 1)
        self.assertEqual(1, len(zl))

        zl = cs.zones.list()
        self.assertEqual(1, len(zl))
        zl = cs.zones.list('zone1')
        self.assertEqual(1, len(zl))

        zl = cs.zones.delete('zone1')
        self.assertEqual(0, len(zl))
        zl = cs.zones.delete('zone1', 1)
        self.assertEqual(0, len(zl))
