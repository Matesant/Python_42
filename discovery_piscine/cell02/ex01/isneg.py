#!/usr/bin/env python3

def main():
	try:
		number = float(input())
	except:
		print("Please enter only numbers.")
		return
	if number == 0:
		print("This number is both positive and negative.")
	elif number < 0:
		print("This number is negative.")
	else:
		print("This number is positive.")
	

if __name__ == "__main__":
	main()