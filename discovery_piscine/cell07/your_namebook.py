#!/usr/bin/env python3
from sys import argv

def array_of_names(persons: dict) -> list:
	array = list(persons.keys())

def main():
	persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
	print(array_of_names(persons))

if __name__ == "__main__":
	main()