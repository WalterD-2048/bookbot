from stats import count_words
from stats import count_characters
from stats import sorted_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv)!= 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    chars_dict = count_characters(text)
    nums_words = count_words(text)
    sort_list = sorted_list(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {nums_words} total words")
    print("--------- Character Count -------")
    for c in sort_list:
        charater = c["character"]
        if charater.isalpha():
            print(f"{charater}: {c['count']}")
    print("============= END ===============")


    


main()
