from utils import *

class tests:
	def reversed_test():
		assert utils.reversed(12345) == 54321
		assert utils.reversed(123.45) == None
		assert utils.reversed("12345") == None
	def formatter_test():
		assert utils.formatter(12345) == ('0b11000000111001', '0o30071')
		assert utils.formatter(123.45) == None
		assert utils.formatter("12345") == None

tests.reversed_test()
tests.formatter_test()
