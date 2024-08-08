#!/usr/bin/env python3

def upcase_it(s: str) -> str:
	if (not isinstance(s, str)):
		return "none"
	return s.upper()

print(upcase_it(1))