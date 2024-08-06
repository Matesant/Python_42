#!/usr/bin/env python3

def main():
	try:
		number = float(input("Give me the first number: "))
		number2 = float(input("Give me the second number: "))
	except:
		print("Error")
		return
	print("Thank you!")
	print(f"{number + number2}")
	print(f"{number - number2}")
	try:
		print(f"{number / number2}")
	except:
		print("Error")
		return
	print(f"{number * number2}")

if __name__ == "__main__":
	main()