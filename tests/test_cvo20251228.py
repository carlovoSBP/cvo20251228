from unittest import TestCase

from cvo20251228 import hello


class TestSmoke(TestCase):
    def test_sanity(self):
        self.assertTrue(True)

    def test_integration(self):
        self.assertEqual("Hello you from cvo20251228!", hello())
