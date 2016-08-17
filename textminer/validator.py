import re


def binary(string):
    return re.match(r'[01]', string)


def binary_even(string):
    return re.match(r'[01]*[0]$', string)


def hex(string):
    return re.match(r'[0-9A-F]+$', string)


def word(string):
    return re.match(r'^[\w]*[-]*[a-z]+$', string)


def words(string, count=0):
    match = re.findall(r'\w*[-]*[a-z]+', string)
    if count == 0:
        return match != []
    else:
        print("MATCH: ", match)
        print(len(match))
        if len(match) == count:
            return match != []


def phone_number(string):
    match = re.match(r'\(*[\d]{3}\)*[-\s\.]*[\d]{3}[-\s\.]*[\d]{4}', string)
    return match


def money(string):
    match = re.match(r'^\$(?:0|[1-9]\d{0,2}(?:,?\d{3})*)(?:\.\d{2})?$', string)
    return match


def zipcode(string):
    match = re.match(r'^\d{5}([-]\d{4})?$', string)
    return match


def date(string):
    date_regex = [r"(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4}|\d{2})",
                  r"(?P<year>\d{4})-?(?P<month>\d{2})-?(?P<day>\d{2})",
                  r"(?P<day>\d{1,2})\s*(?P<month>[A-Za-z]{3})\s*(?P<year>\d{4})",
                  r"(?P<month>[A-Za-z]{3})\s*(?P<day>\d{1,2})\s*,?\s*(?P<year>\d{4})"]

    for regex in date_regex:
        match = re.match(regex, string)
        if match:
            return match
