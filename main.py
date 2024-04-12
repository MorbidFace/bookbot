def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    character_count = get_character_count(text)
    report(words, character_count, book_path)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    lowered_text = text.lower()
    character_set = set()
    character_dict = {}
    for char in lowered_text:
        if (char in character_set):
            character_dict[char] = character_dict[char] + 1
        else:
            character_set.add(char)
            character_dict[char] = 1
    
    return character_dict

def report(words, character_count, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{len(words)} words found in the document")

# def sort_on(dict):
    # return dict[]


main()