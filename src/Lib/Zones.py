import random

zones = ["Costanera", "Chimba", "Muyurina", "Beijing", "Reducto"]
extentions = [100, 130, 140, 90, 200]


def __init__(self):
    self.zones = zones
    self.extentions = extentions


def generateZones():
    return random.randint(1, len(zones))


def generateExtentions():
    return random.randint(1, len(extentions))
