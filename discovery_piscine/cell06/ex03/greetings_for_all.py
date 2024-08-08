#!/usr/bin/env python3

def greetings(name: str = None) -> None:
	if name is None:
		print("Hello, noble stranger")
	elif not (isinstance(name, str)):
		print ("Error! It was not a name.")
	else:
		print(f"Hello, {name}.")

def main():
	greetings()
	greetings("Alice")
	greetings("Bob")
	greetings(1)
	greetings(1.0)
	

if __name__ == "__main__":
	main()