#!/usr/bin/env python3
from sys import argv

def main():
	if (len(argv) == 1):
		print("none")
		return
	print(argv[1])

if __name__ == "__main__":
	main()