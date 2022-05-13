import random

bornPlace = ["Cochabamba", "La Paz", "Sucre", "Oruro", "Potosi", "Santa Cruz", "Pando", "Beni", "Tarija"]


def __init__(self):
    self.bornPlace = bornPlace


def generate():
    bP = bornPlace[random.randint(0, len(bornPlace) - 1)]
    return bP
