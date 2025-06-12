def word_count(wc_book_path):
    with open(wc_book_path) as f:
        wc_book_string = f.read()
        wc = len(wc_book_string.split())
    return f"Found {wc} total words"

def get_character_count(char_book_path):
    chars_dict = {}
    with open(char_book_path) as f:
        full_text = f.read()
        for i in full_text.lower():
            if i not in chars_dict:
                chars_dict[i] = 0
            if i in chars_dict:
                chars_dict[i] += 1
    return chars_dict    

def organize(char_counts):
    list_dict = []
    for char in char_counts:
        count = char_counts[char]
        list_dict.append({"char": char, "num": count})
    def sort_on(d):
        return d["num"]
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict
    






def main():
    print(get_character_count("./books/frankenstein.txt"))


if __name__ == "__main__":
    main()