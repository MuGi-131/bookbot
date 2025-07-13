from stats import get_num_words

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        num_words = count(file_contents)
        print(f'{num_words} words found in the document')

def main():
    get_book_text('./books/frankenstein.txt')

main()
