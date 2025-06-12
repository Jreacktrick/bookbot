import sys
from stats import word_count, get_character_count, organize


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

def get_book_text(book_path):
    with open(book_path) as f:
        book_string = f.read() 
    return f"{book_string}"

def main():
    char_count = get_character_count(book_path)
    char_count_organized = organize(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(word_count(book_path))
    print("--------- Character Count -------")
    for dict_item in char_count_organized:
        if dict_item["char"].isalpha():
            print(f"{dict_item["char"]}: {dict_item["num"]}")



if __name__ == "__main__":
    main()       
