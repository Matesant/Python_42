#!/usr/bin/env python3

def main():
	try:
		number = int(input("Give me the first number: "))
		number2 = int(input("Give me the second number: "))
	except:
		print("Error")
		return
	print("Thank you!")
	print(f"{number} + {number2} = {number + number2}")
	print(f"{number} - {number2} = {number - number2}")
	try:
		print(f"{number} / {number2} = {number // number2}")
	except:
		print("Undefined")
	print(f"{number} * {number2} = {number * number2}")

if __name__ == "__main__":
	main()