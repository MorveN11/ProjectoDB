def joinNames(words):
    wordsList = words.split(",")
    return wordsList


def appendNones(words):
    for i in range(20):
        words.append("-")
    return words
