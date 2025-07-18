from stats import get_num_words, get_count, sort_on
import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    print('============ BOOKBOT ============')
    book_path = sys.argv[1]
    print(book_path)
    print(f'Analyzing book found at {book_path}')
    text = get_book_text(book_path)
    print('----------- Word Count ----------')
    num_words = get_num_words(text)
    print('--------- Character Count -------')
    chars_dict = get_count(text)
    print(f'Found {num_words} total words')
    res = []
    for item in chars_dict:
        if item.isalpha():
            res.append({
                'char': item,
                'num': chars_dict[item]
                })
    res.sort(reverse=True, key=sort_on)
    for i in res:
        print(f"{i['char']}: {i['num']}")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
