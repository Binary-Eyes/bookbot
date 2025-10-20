import sys
from stats import count_words
from stats import generate_char_count
from stats import sort_char_count

def load_book(path):
    with open(path) as f:
        return f.read()
    

def print_report(path):
    text = load_book(path)
    word_count = count_words(text)
    char_count = generate_char_count(text)
    sorted_chars = sort_char_count(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        if (entry["char"].isalpha()):
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")


def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    target_path = sys.argv[1]
    print_report(target_path)

if __name__=="__main__":
    main()
