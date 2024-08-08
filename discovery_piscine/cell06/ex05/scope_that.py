#!/usr/bin/env python3
from sys import argv

def add_one(x: any):
	x += 1

def main():
	x = 0
	print(x)
	add_one(x)
	print(x)

if __name__ == "__main__":
	main()