#!/usr/bin/env python3
def main():
	array = [2, 8, 9, 48, 8, 22, -12, 2]
	array2 = [i + 2 for i in array]
	array3 = [i for i in array2 if i > 5]
	print(array3)

if __name__ == "__main__":
	main()