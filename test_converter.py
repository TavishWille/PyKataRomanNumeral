import unittest
import converter
import inspect


class TestConverter(unittest.TestCase):

	#I used http://www.thecalculatorsite.com/misc/romannumerals.php for all expected values. 

	def setUp(self):
		self.converter = converter.Converter()

	def nameOfTest(self):
		return inspect.stack()[2][3]

	def statusOfTest(self, test_input, expected, result):
		print("\n")
		print("================================================================")
		print("Name of Test: " + self.nameOfTest())
		print("Input: " + str(test_input))
		print("Expected result: " + str(expected))
		print("Actual result: " + str(result))
		print("\n")

	#Testing convert from integer to roman numeral.
	#I know that I want to use a hash table to program this functionality, so I will test the direct hash lookups first, then move on to more interesting cases.

	def test_convert_1_to_I(self):
		test_input = 1
		result = self.converter.convertIntegerToRomanNumeral(test_input)
		expected = "I"
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_5_to_V(self):
		test_input = 5
		result = self.converter.convertIntegerToRomanNumeral(test_input)
		expected = "V"
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_10_to_X(self):
		test_input = 10
		result = self.converter.convertIntegerToRomanNumeral(test_input)
		expected = "X"
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_100_to_C(self):
		test_input = 100
		result = self.converter.convertIntegerToRomanNumeral(test_input)
		expected = "C"
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_4_to_IV(self):
		test_input = 4
		result = self.converter.convertIntegerToRomanNumeral(test_input)
		expected = "IV"
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_2_to_II(self):
		test_input = 2
		result = self.converter.convertIntegerToRomanNumeral(test_input)
		expected = "II"
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_47_to_XLVII(self):
		test_input = 47
		result = self.converter.convertIntegerToRomanNumeral(test_input)
		expected = "XLVII"
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_1234_to_MCCXXXIV(self):
		test_input = 1234
		result = self.converter.convertIntegerToRomanNumeral(test_input)
		expected = "MCCXXXIV"
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_952_to_CMLII(self):
		test_input = 952
		result = self.converter.convertIntegerToRomanNumeral(test_input)
		expected = "CMLII"
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_3888_to_MMMDCCCLXXXVIII(self):
		test_input = 3888
		result = self.converter.convertIntegerToRomanNumeral(test_input)
		expected = "MMMDCCCLXXXVIII"
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	#Max Roman Numeral
	def test_convert_4999_to_MMMMCMXCIX(self):
		test_input = 4999
		result = self.converter.convertIntegerToRomanNumeral(test_input)
		expected = "MMMMCMXCIX"
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)




	#Testing the inverse (converting roman numerals to integers)

	def test_convert_I_to_1(self):
		test_input = "I"
		result = self.converter.convertRomanNumeralToInteger(test_input)
		expected = 1
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_V_to_5(self):
		test_input = "V"
		result = self.converter.convertRomanNumeralToInteger(test_input)
		expected = 5
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_X_to_10(self):
		test_input = "X"
		result = self.converter.convertRomanNumeralToInteger(test_input)
		expected = 10
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_II_to_2(self):
		test_input = "II"
		result = self.converter.convertRomanNumeralToInteger(test_input)
		expected = 2
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_MMMDCCCLXXXVIII_to_3888(self):
		test_input = "MMMDCCCLXXXVIII"
		result = self.converter.convertRomanNumeralToInteger(test_input)
		expected = 3888
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_MDVII_to_1507(self):
		test_input = "MDVII"
		result = self.converter.convertRomanNumeralToInteger(test_input)
		expected = 1507
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_MDCCCLXXXIX_to_1889(self):
		test_input = "MDCCCLXXXIX"
		result = self.converter.convertRomanNumeralToInteger(test_input)
		expected = 1889
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_MCCCXXXVII_to_1337(self):
		test_input = "MCCCXXXVII"
		result = self.converter.convertRomanNumeralToInteger(test_input)
		expected = 1337
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_MCCXXXIV_to_1234(self):
		test_input = "MCCXXXIV"
		result = self.converter.convertRomanNumeralToInteger(test_input)
		expected = 1234
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_XLVII_to_1337(self):
		test_input = "XLVII"
		result = self.converter.convertRomanNumeralToInteger(test_input)
		expected = 47
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

	def test_convert_MMMMCMXCIX_to_4999(self):
		test_input = "MMMMCMXCIX"
		result = self.converter.convertRomanNumeralToInteger(test_input)
		expected = 4999
		self.assertEqual(result, expected)
		if(result == expected):
			self.statusOfTest(test_input, expected, result)

if __name__ == "__main__":
	unittest.main()