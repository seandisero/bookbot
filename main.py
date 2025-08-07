import stats as stt
import sys


def get_book_text(book_path):
    file_contents = ''
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    book = sys.argv[1]
    frankenstein_string = get_book_text(book)
    print('Found {} total words'.format(len(frankenstein_string.split())))
    sorted_letter_count = stt.sort_counted_letters(stt.count_number_of_letters(frankenstein_string))
    for i in sorted_letter_count:
        print('{}: {}'.format(i['char'], i['num']))

if __name__ == "__main__":
    main()
