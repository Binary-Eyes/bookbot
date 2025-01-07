def main():    
    path = './books/frankenstein.txt'
    text = load_book(path)
    word_count = count_words(text)
    char_count = count_chars(text)    
    generate_book_report(path, word_count, char_count)


def count_words(text):
    print('counting words...')
    words = text.split()
    return len(words)


def generate_book_report(path, word_count, char_count):
    print(f'--- begin report of {path} ---')
    print(f'{word_count} words found in the document')
    char_map = generate_char_mapping(char_count)
    char_map.sort(reverse=True, key=sort_on_count)  
    for entry in char_map:
        print(f"The '{entry['name']}' character was found {entry['count']} times")
    print('--- End Report ---')


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