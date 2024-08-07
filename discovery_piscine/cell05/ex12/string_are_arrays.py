#!/usr/bin/env python3
from sys import argv
from re import findall

def main():
	if (len(argv) <= 1):
		print("none")
		return
	argc = len(argv) - 1
	print(f"parameters: {argc}")
	for i in range(1, len(argv)):
		print(f"{argv[i]}: {len(argv[i])}")

if __name__ == "__main__":
	main()