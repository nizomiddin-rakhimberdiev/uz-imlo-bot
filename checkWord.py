from uzwords_latin import words
from difflib import get_close_matches


def checkWords(word, words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    available = False  # bunday so'z mavjud emas

    if word in matches:
        available = True
        matches = word
    # elif "'" in word:
    #     word = word.replace("'", "‘")
    #
    #     # matches.update(get_close_matches(word, words))
    # elif '‘' in word:
    #     word = word.replace('‘', "'", )
    #     # matches.update(get_close_matches(word, words))

    return {'available': available, 'matches': matches}


if __name__ == '__main__':
    print(checkWords("o'zbek"))
    print(checkWords("o'rik"))
