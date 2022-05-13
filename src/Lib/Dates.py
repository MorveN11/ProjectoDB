import random


def dates():
    year = random.randint(1990, 2005)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    birthDay = (str(year) + "/" + str(month) + "/" + str(day))
    return birthDay


def contractDate():
    year = random.randint(2018, 2022)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    contraDate = (str(year) + "/" + str(month) + "/" + str(day))
    return contraDate
