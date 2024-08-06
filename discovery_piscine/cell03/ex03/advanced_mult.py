#!/usr/bin/env python3
from sys import argv

def main():
	argc = len(argv)
	if argc != 1:
		print("none")
		return
	i = 0
	while i <= 10:
		line = ""
		j = 0
		while j <= 10:
			line += f"{i*j} "
			j += 1
		print(f"Table de {i} : {line}")
		i += 1
	

if __name__ == "__main__":
	main()