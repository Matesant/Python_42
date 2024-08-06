#!/usr/bin/env python3

def main():
	try:
		number = str(input("Give me a number: "))
	except ValueError:
		print("Error")
		return
	if number.find(".") != -1:
		print("This number is a decimal.")
	else:
		print("This number is an integer.")
	

if __name__ == "__main__":
	main()