#!/usr/bin/env python3
from sys import argv

def main():
	if (len(argv) != 2):
		print("none")
		return
	needle = argv[1]
	haystack = input("What was the parameter? ")
	if haystack == needle:
		print("Good job!")
	else:
		print("Nope, sorry...")

if __name__ == "__main__":
	main()