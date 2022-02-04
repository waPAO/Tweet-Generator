from histogram import histogram_dictionary
import random

def random_word(histogram: dict) -> str:
    pass

def track_count(loops: int, histogram: dict) -> dict:
    histo_copy = histogram
    words = [word for word in histogram for i in range(histogram[word])]
    for word in histo_copy:
        histo_copy[word] = 0

    for i in range(loops):
        dart = random.randint(1, len(words)) - 1
        word = words[dart]
        histo_copy[word] += 1
    return histo_copy



if __name__ == '__main__':
    histogram = histogram_dictionary('oneFish.txt')
    print(track_count(1000000, histogram))