class Converter:

	#I think a nice way to do this is to use a hash table.  This means a bit of memory usage, however this means that the conversion can be done in one pass...
	#meaning a tight bound of n (this algorithm is completed in linear time).

	#Class constructor... Essentially just two hash tables that cover the letters of the roman numerals. 
	def __init__(self):
		self.values = {}
		self.values["I"] = 1
		self.values["V"] = 5
		self.values["X"] = 10
		self.values["L"] = 50
		self.values["C"] = 100
		self.values["D"] = 500
		self.values["M"] = 1000
		#Since there is a bijection between Roman Numerals in this list and the corresponding integer values 
		#I can flip the keys and values and store them.  This will be useful for converting from int to roman numeral later. 
		self.invertedValues = {}
		for key, value in self.values.items():
			self.invertedValues[value] = key
		#I can also add a couple other useful values here that will make the converting from int to roman numeral easier. 
		#The rules of roman numerals specify that a "subtraction number" must be at least 1/10 the value of the bigger number and can only be I, X or C.
		#This means there are a small number of these values and can be included in the hash tabel to speed things up later. 
		self.invertedValues[900] = "CM"
		self.invertedValues[400] = "CD"
		self.invertedValues[90] = "XC"
		self.invertedValues[40] = "XL"
		self.invertedValues[9] = "IX"
		self.invertedValues[4] = "IV"

	#This is just a wrapper to make it nicer to call the function from outside the class. 
	def convertRomanNumeralToInteger(self, romanNumeral):
		return self.__convertToIntRecursive(romanNumeral, 0)


	def __convertToIntRecursive(self, romNum, runningTotal):
		#If it is empty, just return 0
		if(len(romNum) == 0):
			return 0
		#If it is just a single roman numeral, return that value. 
		if(len(romNum) == 1):
			return self.values[romNum]
		#The recursive step
		#There are really 2 cases to consider, the first being if there is subtraction notation
		#If that is the case, we subtract the lesser number from the bigger and strip off both characters from the string
		if(self.values[romNum[0]] < self.values[romNum[1]]):
			runningTotal = runningTotal + (self.values[romNum[1]] - self.values[romNum[0]]) + self.__convertToIntRecursive(romNum[2:], runningTotal)
			return runningTotal
		#The other case is if there is no subtraction notation.  We just calculate the value and strip off the character. 
		return runningTotal + self.values[romNum[0]] + self.__convertToIntRecursive(romNum[1:], runningTotal)


	def __convertToRomanNumeralRecursive(self, intValue, runningRomNum):
		#The base cases
		if(intValue == 0):
			return ""

		if intValue in self.invertedValues:
			return self.invertedValues[intValue]

			
		#If it is not one of our saved values, we need to do a bit of math:
		
		#First let's find the biggest roman numeral that fits in this integer, I need to keep in mind subtraction notation here 
		largestKey = 0
		for key, value in self.invertedValues.items():
			if(key < intValue and key > largestKey):
				largestKey = key
		runningRomNum = runningRomNum + self.invertedValues[largestKey] + self.__convertToRomanNumeralRecursive(intValue-largestKey, runningRomNum)
		return runningRomNum

	#This is just a wrapper to make it nicer to call the function from outside the class.
	def convertIntegerToRomanNumeral(self, integerValue):
		return self.__convertToRomanNumeralRecursive(integerValue, "")

