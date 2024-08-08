#!/usr/bin/env python3
from sys import argv

def array_of_names(persons: dict) -> list:
    return [f"{key.capitalize()} {value.capitalize()}" for key, value in persons.items()]

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