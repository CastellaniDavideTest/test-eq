"""Test eq file
"""
from eq import *

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2021-1-3"

def test():
	"""Tests the eq function in the eq class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert eq.eq() == "eq", "test failed"
	#assert eq.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
