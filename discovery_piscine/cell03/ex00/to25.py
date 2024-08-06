#!/usr/bin/env python3

def main():
	try:
		number = int(input("Enter a number less than 25\n"))
	except:
		print("Error")
		return
	if number > 25:
		print("Error")
		return
	while True:
		print(f"Inside the loop, my variable is {number}")
		number += 1
		if number == 26:
			break
	

if __name__ == "__main__":
	main()