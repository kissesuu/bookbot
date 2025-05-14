from stats import get_num_words
from stats import get_num_char
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    file_contents = get_book_text(sys.argv[1])

    num_words = get_num_words(file_contents)
    print(num_words)
    contents = get_num_char(file_contents)
    sorted_dict = dict(sorted(contents.items(), key=lambda item: item[1], reverse=True))

    for key, value in sorted_dict.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()