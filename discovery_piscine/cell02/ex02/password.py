#!/usr/bin/env python3

def main():
	password = "Po"
	attempt = input()
	if attempt == password:
		print("ACCESS GRANTED")
	else:
		print("ACCESS DENIED")

if __name__ == "__main__":
	main()