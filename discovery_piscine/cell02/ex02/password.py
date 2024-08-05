#!/usr/bin/env python3

def main():
	password = "Jorge"
	try:
		attempt = int(input())
	except:
		print("Please enter only numbers.")
		return
	if attempt == password:
		print("ACCESS GRANTED")
	else:
		print("ACCESS DENIED")

if __name__ == "__main__":
	main()