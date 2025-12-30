import sys
from stats import get_num_words, get_num_chars, get_sorted_chars


def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    get_num_words(text)
    print("--------- Character Count -------")
    counted_chars = get_num_chars(text)
    get_sorted_chars(counted_chars)
    print("============= END ===============")


main()
