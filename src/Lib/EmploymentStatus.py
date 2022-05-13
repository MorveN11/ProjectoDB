import random

employmentStatus = ['activo', 'inactivo', 'enfermo', 'receso', 'activo', 'activo', 'activo', 'activo']


def __init__(self):
    self.employmentStatus = employmentStatus


def generate():
    eS = employmentStatus[random.randint(0, len(employmentStatus) - 1)]
    return eS
