import re


def run_my_test(match, text):
    if match == None or text == "":
        return False
    else:
        return match.group() == text


def binary(text):
    match = re.search(r"[01]*", text)
    return match.group()

def binary_even(text):
    match = re.search(r"[01]*0$", text)
    return run_my_test(match, text)

def hex(text):
    match = re.search(r"[0-9A-F]+", text)
    return run_my_test(match, text)


def word(text):
    match = re.search(r"[\w-]*[a-z]+", text)
    return run_my_test(match, text)

"""
def words(text):
    if len(text) < 1:
        return False

    for characters in text.split():
        searched = re.search(r"[\w-]*[a-z]+", characters)
        if searched is None or searched.group() != characters:
            return False

    if not count:
        return True
    elif count == len(text.split()):
        return True,
    else:
        return False
"""

def phone_number(text):
    match = re.search(r"\(?\d{3}[\)-\.]? ?\d{3}[-\.]?\d{4}", text)
    print(match)
    return run_my_test(match, text)


def money(text):
    match = re.search(r"^\$\d+(?:,\d{3})*(?:\.\d{2})?", text)
    return run_my_test(match, text)


def zipcode(text):
    match = re.search(r"^\d{5}(?:-\d{4})?", text)
    return run_my_test(match, text)

# def date(text)