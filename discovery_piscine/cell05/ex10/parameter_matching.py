#!/usr/bin/env python3
from sys import argv
from re import findall

def main():
	if (len(argv) != 2):
		print("none")
		return
	needle = argv[1]
	haystack = input("What was the parameter? ")
	if haystack.find(needle) == -1:
		print("Nope, sorry...")
	else:
		print("Good job!")

if __name__ == "__main__":
	main()