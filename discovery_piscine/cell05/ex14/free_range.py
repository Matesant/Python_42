#!/usr/bin/env python3
from sys import argv
from re import findall

def main():
	try:
		if (len(argv) != 3):
			print("none")
			return
		number1 = int(argv[1])
		number2 = int(argv[2])
		if number1 < number2:
			array = list(range(number1, number2 + 1))
		else:
			array = list(range(number2, number1 + 1))
		print(array)
	except:
		print("none")
		return

if __name__ == "__main__":
	main()