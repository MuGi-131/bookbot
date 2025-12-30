def get_num_words(text):
    num_words = len(text.split())
    print(f"Found {num_words} total words")


def get_num_chars(text):
    text = text.lower()
    chars = []
    count = 0
    counted = {}

    for char in text:
        if char not in chars:
            chars.append(char)
            counted[char] = 1
        else:
            counted[char] += 1
    print(counted)
