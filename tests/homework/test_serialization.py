import unittest

from tests.homework.config import CESAR


class Main(unittest.TestCase):

    def setUp(self):
        self.cesar = CESAR

    def test_yaml(self):
        print(self.cesar)

