#!/usr/bin/env python

def main():
	try:
		number = float(input())
	except NameError:
		print("Error")
		return
	if number == 0:
		print("This number is equal to zero.")
	else: 
		print("This number is different from zero.")

if __name__ == "__main__":
	main()