def count_words(text):
    return len(text.split())

def count_letters(text):
    count = {}
    for ch in text:
        lower_ch = ch.lower()
        if lower_ch not in count:
            count[lower_ch] = 0
        count[lower_ch] += 1
    return count

def get_sorted(counted_chars):
    sorted = []
    for entry in counted_chars:
        sorted.append({"char": entry, "num": counted_chars[entry]})

    sorted.sort(reverse=True, key=sort_by_num)
    return sorted
    
def sort_by_num(input):
    return input["num"]