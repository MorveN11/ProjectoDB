import random

civilStatus = ["Casado", "Viudo", "Soltero", "Divorciado"]


def __init__(self):
    self.civilStatus = civilStatus


def generate():
    cS = civilStatus[random.randint(0, len(civilStatus) - 1)]
    return cS
