#!/usr/bin/env python

def main():
	try:
		number = int(input())
	except:
		print("Please enter only numbers.")
		return
	if number == 0:
		print("This number is equal to zero.")
	else: 
		print("This number is different from zero.")

if __name__ == "__main__":
	main()