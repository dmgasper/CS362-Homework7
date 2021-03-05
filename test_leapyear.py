import leapyear
import unittest

class TestLeapYear(unittest.TestCase):

	def test_isleapyear(self):
		result = leapyear.isLeapYear(2012)
		self.assertEqual(result, True)
