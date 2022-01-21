from random import shuffle
from sys import argv

def rearrange(random_words: list) -> str:
    shuffle(random_words)
    str_form = ' '
    return str_form.join(random_words)

if __name__ == '__main__':
    word_inputs = argv[1:]
    random_words = rearrange(word_inputs)
    print(random_words)