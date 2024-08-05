#!/usr/bin/env python3

def main():
	number1 = input("Enter the first number:")
	number2 = input("Enter the second number:")
	try:
		result = int(number1) * int(number2)
	except:
		print("Please enter only numbers.")
		return
	print(f"{number1} * {number2} = {result}")
	if result < 0:
		print("The result is negative.")
	else:
		print("The result is positive.")

if __name__ == "__main__":
	main()