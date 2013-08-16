#__author__ = 'wattanai'
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_something_wrong(self):
        self.assertEquals(True, True)

    def test_Ho_Lee_Fuk(self):
        self.assertEquals(True, False)


if __name__ == '__main__':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)
