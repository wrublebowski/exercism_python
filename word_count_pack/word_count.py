import re

txt = " multiple   whitespaces"


def count_words(sentence):
    sentlist = re.split(', |,| |_|\t|\n', sentence.lower())

    # def a func to filter words:
    def remover(word):

        for i in word:

            if i in re.findall('\W', word) and i != "'":
                word = word.replace(i, '')
            if word.count("'") >= 2:
                word = word.replace("'", '')
        return word

    # convert string into 'pure' list:
    x = list(map(remover, sentlist))

    # create new dictionary, ignoring whitespaces:
    result = {}

    for item in x:
        if item != '':
            result[item] = x.count(item)

    print (result)
    return result

count_words(txt)