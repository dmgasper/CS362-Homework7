import unittest
import fizzbuzz
class TestListAverage(unittest.TestCase):

	def test_fizz(self):
		result = fizzbuzz.getOutput(3)
		self.assertEqual(result, "Fizz")
		
	def test_buzz(self):
		result = fizzbuzz.getOutput(5)
		self.assertEqual(result, "Buzz")
		
	def test_buzz(self):
		result = fizzbuzz.getOutput(15)
		self.assertEqual(result, "FizzBuzz")
		
	def test_buzz(self):
		result = fizzbuzz.getOutput(16)
		self.assertEqual(result, 16)

		
if __name__ == "__main__":
	unittest.main()
