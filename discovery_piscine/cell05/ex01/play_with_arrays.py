#!/usr/bin/env python3
def main():
	array = [2, 8, 9, 48, 8, 22, -12, 2]
	array2 = [i + 2 for i in array]
	print(f"Original array: {array}")
	print(f"New array: {array2}")

if __name__ == "__main__":
	main()
