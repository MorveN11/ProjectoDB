import random

results = ["aceptado", "rechazado", "rechazado"]


def __init__(self):
    self.results = results


def numGenerate():
    n = random.randint(0, 100)
    return n


def worGenerate():
    res = results[random.randint(0, len(results)-1)]
    return res
