def main():
	name = input("Hey, what's your first name? : ").strip().capitalize()
	last_name = input("And your last name? : ").strip()
	print(f"Well, pleased to meet you, {name} {last_name}.")

if __name__ == "__main__":
	main()