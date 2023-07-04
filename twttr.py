def main():
    text = input("Enter the text: ")
    removeVowels = shorten(text)
    print(removeVowels)


def shorten(word):
    vowels = "AEIOUaeiou"
    new_String = ''
    for i in word:
        if i not in vowels:
            new_String += i
    return new_String


if __name__ == "__main__":
    main()
