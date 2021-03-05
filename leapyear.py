def isLeapYear(input):
	if (input % 4 == 0 and input % 100 != 0 and input % 400 != 0): return True
	else: return False
