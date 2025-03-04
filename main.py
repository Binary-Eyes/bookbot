from stats import count_words

def main():    
    path = './books/frankenstein.txt'
    text = load_book(path)
    word_count = count_words(text)
    char_count = count_chars(text)    
    generate_book_report(path, word_count, char_count)


def generate_book_report(path, word_count, char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")    
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_map = generate_char_mapping(char_count)
    char_map.sort(reverse=True, key=sort_on_count)  
    for entry in char_map:
        print(f"{entry['name']}: {entry['count']}")
    print("============= END ===============")


def generate_char_mapping(char_count):
    chars = []
    for ch in char_count:
        chars.append({"name": ch, "count": char_count[ch]})
    return chars


def sort_on_count(char_map):
    return char_map["count"]


def count_chars(text):
    print('counting alphabet characters...')
    map = {}
    for ch in text:
        if not ch.isalpha():
            continue
        ch = ch.lower()
        if ch not in map:
            map[ch] = 1
        else:
            map[ch] += 1
    return map
    

def load_book(path):
    print(f'loading book: {path}')
    with open(path) as f:
        return f.read()        
    

main()