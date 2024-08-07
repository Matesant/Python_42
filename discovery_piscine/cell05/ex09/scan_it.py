#!/usr/bin/env python3
from sys import argv
from re import findall

def main():
	if (len(argv) != 3):
		print("none")
		return
	needle = argv[1]
	haystack = argv[2]
	print(len(findall(needle, haystack)))

if __name__ == "__main__":
	main()