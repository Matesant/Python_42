#!/usr/bin/env python3
from sys import argv
from re import findall

def main():
	if (len(argv) != 2):
		print("none")
		return
	needle = "z"
	haystack = argv[1]
	z_ocurrences = findall(needle, haystack)
	if z_ocurrences == []:
		print("none")
	else:
		print(''.join(z_ocurrences))

if __name__ == "__main__":
	main()