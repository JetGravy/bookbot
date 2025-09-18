from stats import count_words, count_characters, sort_letters

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
    
    # Get report
    input: str = 'books/frankenstein.txt'
    book_text: str = get_book_text(input)
    word_count: int = count_words(book_text)
    log = count_characters(book_text)
    
    # Print report
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {input}...')
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for entry in log:
        if entry["char"].isalpha():
            print(f'{entry["char"]}: {entry["num"]}')

    print("============= END ===============")


if __name__ == "__main__":
    main()