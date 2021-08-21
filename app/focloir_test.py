from focloir import Focloir
import random

WORDS = open("/usr/share/dict/words").read().splitlines()
TOT_WORDS = len(WORDS)
#amount of words to test on
WORD_LIMIT = 20

def test_words():
    words = get_random_words(WORD_LIMIT)
    focloir = Focloir()
    for word in words:
        translation = focloir.translate(word)
        print("{} => {}".format(word, translation))
    return

def get_random_word():
    return WORDS[random.randint(0, TOT_WORDS)]

def get_random_words(limit=0):
    words = []
    if limit == 0:
        print("No word limit set, please set a limit")
        return
    else:
        for i in range(limit):
            words.append(get_random_word())
    return words

def main():
    test_words()
    return

if __name__ == '__main__':
    main()