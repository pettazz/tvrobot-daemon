import unittest

from core.strings import Stringifier

class BaseModelTest(unittest.TestCase):

    def setUp(self):
        #TODO: stub some test strings into core.strings.STRINGS rather than relying on some random one that may change
        pass

    def tearDown(self):
        pass

    def test_simple_stringification(self):
        self.s = Stringifier('en-US')
        self.assertEqual(self.s.tvrobot.add_completed, "Beeped the new torrent.", 'Mismatched stringification result')

    def test_default_lang(self):
        self.s = Stringifier()
        self.assertEqual(self.s.tvrobot.add_completed, "Beeped the new torrent.", 'Mismatched stringification result')

    def test_fallback_lang(self):
        self.s = Stringifier('fi-FI')
        self.assertEqual(self.s.tvrobot.add_completed, "Beeped the new torrent.", 'Mismatched stringification result')

    def test_missing_key(self):
        self.s = Stringifier('en-US')
        self.assertEqual(self.s.tvrobot.bananahammock, "[tvrobot.bananahammock]", 'Mismatched stringification result')

    def test_missing_category(self):
        self.s = Stringifier('en-US')
        self.assertEqual(self.s.bananahammock.butts, "[bananahammock.butts]", 'Mismatched stringification result')

