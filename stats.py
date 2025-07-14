def  get_num_words(content):
    tmp = content.split()
    return len(tmp)

def get_count(content):
    tmp = list(content.lower())
    arr = []
    res = {}
    for char in tmp:
        if char not in arr:
            arr.append(char)
    for char in arr:
       res[char]=tmp.count(char)
    return res

def sort_on(items):
    return items['num']
