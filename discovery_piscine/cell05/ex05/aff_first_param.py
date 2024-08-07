#!/usr/bin/env python3
from sys import argv

def main():
	if (len(argv) == 1):
		print("none")
		return
	elif (len(argv) > 2):
		print("Too many arguments")
		return
	print(argv[1])

if __name__ == "__main__":
	main()