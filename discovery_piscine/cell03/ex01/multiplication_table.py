#!/usr/bin/env python3

def main():
	try:
		number = int(input("Enter a number\n"))
	except:
		print("Error")
		return
	for i in range(10):
		print(f"{i} x {number} =  {number * i}")
	

if __name__ == "__main__":
	main()