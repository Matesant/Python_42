#!/usr/bin/env python3
from sys import argv

def main():
	if (len(argv) < 2):
		print("none")
		return
	needle = "ism"
	for i in range(1, len(argv)):
		if argv[i].endswith(needle):
			continue
		else:
			print(f"{argv[i]}{needle}")
	

if __name__ == "__main__":
	main()