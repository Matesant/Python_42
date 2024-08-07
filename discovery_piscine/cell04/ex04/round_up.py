#!/usr/bin/env python3
from math import ceil

def main():
	try:
		number = float(input("Give me a number: "))
		print(ceil(number))
	except ValueError:
		print("Error")
	

if __name__ == "__main__":
	main()