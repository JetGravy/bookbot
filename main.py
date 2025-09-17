from stats import count_words

'''
    take in file path of book, output as string
'''
def get_book_text(book_path: str):
    with open(book_path) as f:
        book_contents: str = f.read()
    return book_contents



'''
    main
'''
def main():
    print("starting up...")
    input: str = './books/frankenstein.txt'
    book_text: str = get_book_text(input)
    word_count: int = count_words(book_text)
    print(f"{word_count} words found in the document")

if __name__ == "__main__":
    main()