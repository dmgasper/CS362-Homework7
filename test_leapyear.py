import leapyear
import unittest

class TestLeapYear(unittest.TestCase):

	def test_isleapyear(self):
		result = leapyear.isLeapYear(2012)
		self.assertEqual(result, True)
		
	def test_isnotleapyear(self):
		result = leapyear.isLeapYear(2019)
		self.assertEqual(result, False)
		
if __name__ == "__main__":
	unittest.main()
