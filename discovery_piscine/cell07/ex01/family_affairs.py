#!/usr/bin/env python3
from sys import argv

def find_the_redheads(persons: dict) -> list:
    return [key.capitalize() for key, value in persons.items() if value == "red"]

def main():
	dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
	print(find_the_redheads(dupont_family))

if __name__ == "__main__":
	main()