#!/usr/bin/env python3
from sys import argv

def downcase_it(s: str) -> str:
	if (not isinstance(s, str)):
		return "none"
	return s.lower()

def main():
	if (len(argv) < 2):
		print("none")
		return
	for i in range(1, len(argv)):
		print(downcase_it(argv[i]))

if __name__ == "__main__":
	main()