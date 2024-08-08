#!/usr/bin/env python3
from sys import argv

def main():
	if (len(argv) < 3):
		print("none")
		return
	for i in range(len(argv) - 1, 0, -1):
		print(argv[i])

if __name__ == "__main__":
	main()
