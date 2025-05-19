import sys
from stats import count_words
from stats import count_letters
from stats import get_sorted

def load_book(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    bookPath = sys.argv[1]
    text = load_book(bookPath)
    word_count = count_words(text)
    counted_chars = count_letters(text)
    sorted_count = get_sorted(counted_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookPath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_count:
        ch = entry["char"]
        num = entry["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
    print("============= END ===============")

main()