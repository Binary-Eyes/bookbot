def count_words(text):
    words = text.split()
    return len(words)

def count_unique_chars(text):
    pass

with open("./books/frankenstein.txt") as f:
    text = f.read()
    print(f'word count: {count_words(text)}')
    