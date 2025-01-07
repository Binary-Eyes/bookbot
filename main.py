def main():    
    text = load_book("./books/frankenstein.txt")
    word_count = count_words(text)
    print(f'word count: {word_count}')

def count_words(text):
    print('counting words...')
    words = text.split()
    return len(words)

def count_unique_chars(text):
    pass

def load_book(path):
    print(f'loading book: {path}')
    with open(path) as f:
        return f.read()        
    
main()