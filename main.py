def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content


def count_word(text):
    num_words = len(text.split())
    print(f"Found {num_words} total words")


def main():
    text = get_book_text("books/frankenstein.txt")
    count_word(text)


main()
