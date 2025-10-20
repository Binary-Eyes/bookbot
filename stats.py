def count_words(source_text):
    return len(source_text.split())


def sort_by_num(items):
    return items["num"]


def sort_char_count(char_counts):
    map = []
    for ch in char_counts:
        map.append({"char": ch, "num": char_counts[ch]})

    map.sort(reverse=True, key=sort_by_num)
    return map


def generate_char_count(source_text):
    count = {}
    for ch in source_text:
        c = ch.lower()
        if c not in count:
            count[c] = 0
        count[c] += 1

    return count