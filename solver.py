import random

words = []
# with open('5_letter_words_com.txt', 'r') as in_file:
with open('5_letter_words_wordle.txt', 'r') as in_file:
# with open('sm_5_letter_words.txt', 'r') as in_file:
    for line in in_file:
        words.append(line.strip())

def get_words_containing(word_list, letter_list):
    containing_words = []
    for word in word_list:
        match = True
        for letter in letter_list:
            if letter not in word:
                match = False

        if match:
            containing_words.append(word)
    
    return containing_words

def get_words_not_containing(word_list, letter_list):
    not_containing_words = []
    for word in word_list:
        match = True
        for letter in letter_list:
            if letter in word:
                match = False

        if match:
            not_containing_words.append(word)
    
    return not_containing_words

def get_words_matching(word_list, pattern_string):
    pattern = {}
    index = 0
    for char in pattern_string:
        if char != '_':
            pattern[index] = char

        index = index + 1

    matching_words = []
    for word in word_list:
        match = True
        for key in pattern:
            if word[key] != pattern[key]:
                match = False

        if match:
            matching_words.append(word)

    return matching_words


def get_words_not_matching(word_list, pattern_string):
    pattern = {}
    index = 0
    for char in pattern_string:
        if char != '_':
            pattern[index] = char

        index = index + 1

    not_matching_words = []
    for word in word_list:
        match = True
        for key in pattern:
            if word[key] == pattern[key]:
                match = False

        if match:
            not_matching_words.append(word)

    return not_matching_words


prog = True
print(random.choice(words))
while prog:
    data = input('Input green pattern, yellow pattern, and grey letters... ("q" to quit)\r\n')
    if data == 'q':
        prog = False
        continue
    data = data.split(' ')
    words = get_words_not_containing(words, data[2])
    words = get_words_matching(words, data[0])
    words = get_words_not_matching(words, data[1])
    words = get_words_containing(words, data[1].replace('_', ''))
    # print(words)
    if len(words) == 0:
        print('No more words in dictionary :(')
        prog = False
        continue
    print(random.choice(words))