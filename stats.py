def get_num_words(text):
    num_words = len(text.split())
    print(f"Found {num_words} total words")


def get_num_chars(text):
    text = text.lower()
    chars = []
    counted = {}

    for char in text:
        if char not in chars:
            chars.append(char)
            counted[char] = 1
        else:
            counted[char] += 1
    return counted


def get_sorted_chars(counted_chars):
    def on_sort(items):
        return items["num"]

    formated = []
    for char in counted_chars:
        if not char.isalpha():
            continue
        formated.append({"char": char, "num": counted_chars[char]})

    formated.sort(reverse=True, key=on_sort)

    for item in formated:
        print(f"{item['char']}: {item['num']}")
