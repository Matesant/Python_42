#!/usr/bin/env python3
from sys import argv

def average(persons: dict) -> list:
    return [key.capitalize() for key, value in persons.items() if value == "red"]

#!/usr/bin/env python3
from sys import argv

def average(persons: dict) -> list:
    for key, value in persons.items():
         avarage_class = sum(persons.values()) / len(persons)
    return avarage_class

def main():
    class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9
    }
    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
    }
    print(average(class_3B))
    print(average(class_3C))

if __name__ == "__main__":
	main()