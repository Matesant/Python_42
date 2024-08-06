#!/usr/bin/env python3

def main():
	input("What you gotta say?: ")
	while True:
		answer = input("I got that! Anything else?: ")
		if answer == "STOP":
			break
	
if __name__ == "__main__":
	main()	