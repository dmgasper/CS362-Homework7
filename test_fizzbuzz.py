import unittest
import fizzbuzz
class TestListAverage(unittest.TestCase):

	def test_fizz(self):
		result = fizzbuzz.getOutput(3)
		self.assertEqual(result, "Fizz")

		
if __name__ == "__main__":
	unittest.main()
