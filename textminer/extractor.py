import re


def phone_numbers(string):
    try:
        result = re.findall(r'\([\d]{3}\)\s\d{3}-\d{4}', string)
        return result
    except:
        return None


def emails(string):
    try:
        result = re.findall(r'[\w.]+@[\w]+\.[\w]{2,}', string)
        return result
    except:
        return None
