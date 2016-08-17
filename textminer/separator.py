import re


def words(string):
    result = re.findall(r'\S+?[A-Za-z]+', string)
    if result:
        return result
    else:
        return None


def phone_number(string):
    phone = {}
    try:
        area, number1, number2 = re.match(r'\(*([\d]{3})\)*[-\s\.]*([\d]{3})[-\s\.]*([\d]{4})', string).groups()
        phone['area_code'] = area
        phone['number'] = number1 + "-" + number2
        print(phone)
        return phone
    except:
        return None


def money(string):
    result = {}
    try:
        groups = re.match(r'^(\$)([1-9\d]+(,\d{3})*(\.\d{2})?)$', string).groups()
        result["currency"] = groups[0]
        result["amount"] = float(re.sub(r',', '', groups[1]))
        return result
    except:
        return None


def zipcode(string):
    result = {}
    try:
        standard, plus4 = re.match(r'^(\d{5})[-]?(\d{4})?$', string).groups()
        result['zip'] = standard
        result['plus4'] = plus4
        return result
    except:
        return None

def date(string):
    date_regex = [r"(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4}|\d{2})",
                  r"(?P<year>\d{4})-?(?P<month>\d{2})-?(?P<day>\d{2})",
                  r"(?P<day>\d{1,2})\s*(?P<month>[A-Za-z]{3})\s*(?P<year>\d{4})",
                  r"(?P<month>[A-Za-z]{3})\s*(?P<day>\d{1,2})\s*,?\s*(?P<year>\d{4})"]

    for regex in date_regex:
        match = re.match(regex, string)
        if match:
            print(match)
            return match
