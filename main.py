from stats import get_num_words


def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content


def main():
    text = get_book_text("books/frankenstein.txt")
    get_num_words(text)


main()
