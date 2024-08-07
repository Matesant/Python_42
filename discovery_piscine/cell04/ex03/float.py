#!/usr/bin/env python3

def main():
	try:
		number = float(input("Give me a number: "))
		number_in_string = str(number)
		dot_position = number_in_string.find(".")
		if (number_in_string[dot_position:]) != '.0':
			print("This number is a decimal.")
		else:
			print("This number is an integer.")
	except ValueError:
		print("Error")
	

if __name__ == "__main__":
	main()