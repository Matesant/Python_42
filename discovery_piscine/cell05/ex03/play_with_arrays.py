#!/usr/bin/env python3
def main():
	array = [2, 8, 9, 48, 8, 22, -12, 2, 10, 10, 2, 2, 3, 8, 8]
	set = {i + 2 for i in array if i > 5}
	print(array)
	print(set)

if __name__ == "__main__":
	main()