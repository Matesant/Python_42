#!/usr/bin/env python3
from sys import argv

def main():
	if (len(argv) != 2):
		print("none")
		return
	print(argv[1].lower())
	
if __name__ == "__main__":
	main()