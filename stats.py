'''
    counts the amount of words in the book
'''
def count_words(book: str):
    return len(book.split())

'''
    counts the occurence of each character in the book
'''
def count_characters(book: str) -> dict [str, int]:
    words = book.lower().split()

    letters: dict [str, int] = {}

    for word in words:
        for char in word:
            if char in letters:
                letters[char] += 1
            else:
                letters.update({f'{char}': 1})

    return sort_letters(letters)

'''
    helper function
'''
def sort_on(items):
    return items["num"]

'''
    sorts the letter counts
'''
def sort_letters(log: dict [str, int]) -> list [dict [str, str], dict [str, int]]: 
    report: list [dict [str, str], dict [str, int]] = []
    for k, v in log.items():
        report.append({"char": f'{k}', "num": v})

    report.sort(reverse=True, key=sort_on)
    
    return report



