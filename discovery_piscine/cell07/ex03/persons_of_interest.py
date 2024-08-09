#!/usr/bin/env python3
from sys import argv

def sort(elem):
    return int(elem[1]["date_of_birth"])

def famous_births(persons: dict) -> None:
    sorted_persons = sorted(persons.items(), key=sort)
    for person in sorted_persons:
        print(f"{person[1]['name']} is a great scientist born in {person[1]['date_of_birth']}")

def main():
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "11878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }
    famous_births(women_scientists)

if __name__ == "__main__":
    main()

women_scientists = {
        "ada": None,
        "cecilia": None,
        "lise": None,
        "grace": None
    }