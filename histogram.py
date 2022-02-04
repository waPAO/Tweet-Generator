import random

def histogram_dictionary(file) -> dict:
    with open(file, 'r') as f:
        words = f.read().split()
        histogram = {}

        for word in words:
            if word not in histogram:
                histogram[word] = 1
            else:
                histogram[word] += 1

        return histogram


def histogram_list(file) -> list:
    with open(file, 'r') as f:
        words = f.read().split()
        histogram = []

        for word in words:
            count = 0
            for other_word in words:
                if word == other_word:
                    count += 1
            if [word, count] not in histogram:
                histogram.append([word, count])
        
        return histogram


def unique_words(histogram) -> int:
    return len(histogram)


def frequency(word: str, histogram) -> int:
    if type(histogram) == dict:
        return histogram[word]
    else:
        for pair in histogram:
            if pair[0] == word:
                return pair[1]


def random_word(histogram) -> str:
    return random.choice(histogram)[0]

    
if __name__ == '__main__':
    dictionary_histogram = histogram_dictionary('oneFish.txt')
    list_histogram = histogram_list('oneFish.txt')
    # print(dictionary_histogram)
    # print(list_histogram)
    # print(unique_words(dictionary_histogram))
    # print(unique_words(list_histogram))
    # print(frequency('fish', dictionary_histogram))
    # print(frequency('fish', list_histogram))
    print(random_word(list_histogram))