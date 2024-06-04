def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_number_of_characters(text):
    characters = {}
    for character in text.lower():
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def print_report(path):
    print(f"--- Begin report of {path} ---\n")
    with open("books/frankenstein.txt") as f:
        text = f.read()
        amnt_words = get_number_of_words(text)
        print(f"{amnt_words} words found in the document\n")
        amnt_characters = get_number_of_characters(text)
        amnt_characters_sorted = dict(sorted(amnt_characters.items(), key=lambda item:item[1], reverse=True))
        for character in amnt_characters_sorted:
            if character.isalpha():
                print(f"The '{character}' character was found {amnt_characters_sorted[character]}")
        print("--- End report ---")


def main():
    print_report("books/frankenstein.txt")

if __name__ == "__main__":
    main()