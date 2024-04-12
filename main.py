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
    dict_list = make_dict_list(character_count)
    dict_list.sort(reverse=True, key=sort_on)
    print()
    for char in dict_list:
        print(f"The '{char["char"]}' character was found {char["count"]} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

def make_dict_list(dict):
    dict_list = []
    alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x','y','z'}
    character_set = set(alphabet)
    for char in dict:
        if (char in character_set):
            char_dict = {
                "char": char,
                "count": dict[char]
            }
            dict_list.append(char_dict)
        
    return dict_list


main()