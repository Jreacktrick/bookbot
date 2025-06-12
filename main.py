

def get_book_text(book_path):
    with open(book_path) as f:
        book_string = f.read() 
    return f"{book_string}"

from stats import word_count, get_character_count, organize

char_count = get_character_count("./books/frankenstein.txt")
char_count_organized = organize(char_count)
#char_count_organized.sort(reverse=True, key=count)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(word_count("./books/frankenstein.txt"))
    print("--------- Character Count -------")
    for dict_item in char_count_organized:
        if dict_item["char"].isalpha():
            print(f"{dict_item["char"]}: {dict_item["num"]}")

if __name__ == "__main__":
    main()       
