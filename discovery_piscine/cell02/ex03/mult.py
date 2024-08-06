#!/usr/bin/env python3

def main():
	try:
		number1 = int(input("Enter the first number:\n"))
		number2 = int(input("Enter the second number:\n"))
	except:
		print("Please enter only integers.")
		return
	result = (number1) * (number2)
	print(f"{number1} X {number2} = {result}")
	if result == 0:
		print("The result is positive and negative.")
	elif result < 0:
		print("The result is negative.")
	else:
		print("The result is positive.")
		

if __name__ == "__main__":
	main()