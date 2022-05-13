import random

emails = ["gmail", "hotmail", "outlook", "icloud", "yahoo", "paoloGod", "fundacion-jala", "gmail", "hotmail", "outlook",
          "icloud", "yahoo", "gmail", "hotmail", "outlook", "icloud", "yahoo", "gmail", "hotmail", "outlook", "icloud",
          "yahoo", "gmail", "hotmail", "outlook", "icloud", "yahoo"]


def __init__(self):
    self.emails = emails


def generate(name):
    email = str(name.lower() + "@" + emails[random.randint(0, len(emails) - 1)] + ".com")
    return email
