import random

aceptList = ["Perfecto", "Tienes lo necesario", "Muy bien", "Buen Trabajo", "Te veo el lunes"]
rechList = ["Te falto muy poco", "Para la próxima", "Necesitas mejorar", "Un poco más de esfuerzo",
            "Respuestas ambiguas", "Copiado de Internet", "Intercambio de respuestas",
            "Tardaste demasiado"]


def __init__(self):
    self.aceptList = aceptList
    self.rechList = rechList


def aceptGenerate():
    feedback = aceptList[random.randint(0, len(aceptList)-1)]
    return feedback


def rechGenerate():
    feedback = rechList[random.randint(0, len(rechList)-1)]
    return feedback
