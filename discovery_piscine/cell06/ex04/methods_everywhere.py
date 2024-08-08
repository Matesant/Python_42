#!/usr/bin/env python3
from sys import argv

def shrink(s: str) -> None:
	if (not isinstance(s, str)):
		return "none"
	print(s[:8])

def enlarge(s: str) -> None:
	if (not isinstance(s, str)):
		return "none"
	while len(s) < 8:
		s += "Z"
	print(s)

def main():
	if (len(argv) < 2):
		print("none")
		return
	for i in range(1, len(argv)):
		if len(argv[i]) < 8:
			enlarge(argv[i])
		else:
			shrink(argv[i])

if __name__ == "__main__":
	main()