def main():
    greeting = input("Enter Text: ").strip().lower()
    results = bank(greeting)
    print(results)


def bank(word):
    if word.startswith("hello"):
        return f"$0"
    elif word.startswith("h"):
        return f"$20"
    else:
        return f"$100"


if __name__ == "__main__":
    main()
