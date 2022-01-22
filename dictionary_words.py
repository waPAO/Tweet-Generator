from random import choices
from sys import argv

def make_sentence(file, num_of_words: int) -> str:
    with open(file, 'r') as f:
        words = f.readlines()
        random_words = choices(words, k=int(num_of_words))

        stripped_words = []
        for word in random_words:
            stripped_words.append(word.strip())

        sentence = ' '
        return sentence.join(stripped_words)

if __name__ == '__main__':
    num_words = argv[1]
    random_sentence = make_sentence('/usr/share/dict/words', num_words)
    print(random_sentence)
