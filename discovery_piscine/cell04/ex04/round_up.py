#!/usr/bin/env python3
from math import ceil

def main():
	try:
		number = float(input("Give me a number: "))
	except ValueError:
		print("Error")
		return
	print(ceil(number))
	

if __name__ == "__main__":
	main()