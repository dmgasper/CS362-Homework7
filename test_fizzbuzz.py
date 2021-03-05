import unittest
import fizzbuzz
class TestListAverage(unittest.TestCase):

	def test_fizz(self):
		result = fizzbuzz.getOutput(3)
		self.assertEqual(result, "Fizz")
		
	def test_buzz(self):
		result = fizzbuzz.getOutput(5)
		self.assertEqual(result, "Buzz")

		
if __name__ == "__main__":
	unittest.main()
