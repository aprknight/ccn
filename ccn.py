import re
from itertools import cycle

# credit Kelvin Zhang for the regular expressions
# https://medium.com/hootsuite-engineering/a-comprehensive-guide-to-validating-and-formatting-credit-cards-b9fa63ec7863
MASTERCARD = re.compile(r'^5[1-5][0-9]{14}$|^2(?:2(?:2[1-9]|[3-9][0-9])|[3-6][0-9][0-9]|7(?:[01][0-9]|20))[0-9]{12}$')
VISA = re.compile(r'^4[0-9]{12}(?:[0-9]{3})?$')
DISCOVER = re.compile(r'^65[4-9][0-9]{13}|64[4-9][0-9]{13}|6011[0-9]{12}|(622(?:12[6-9]|1[3-9][0-9]|[2-8][0-9][0-9]|9[01][0-9]|92[0-5])[0-9]{10})$')
JCB = re.compile(r'^(?:2131|1800|35[0-9]{3})[0-9]{11}$')
AMEX = re.compile(r'^3[47][0-9]{13}$')
DINERS = re.compile(r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$')
MAESTRO = re.compile(r'^(5018|5081|5044|5020|5038|603845|6304|6759|676[1-3]|6799|6220|504834|504817|504645)[0-9]{8,15}$')

# the following dictionaries are used to optimise the calculations required in the implementation of the Luhn algorithm
LMAP = {
    '0': 0,
    '1': 2,
    '2': 4,
    '3': 6,
    '4': 8,
    '5': 1,
    '6': 3,
    '7': 5,
    '8': 7,
    '9': 9
}

NMAP = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

# validates a string of numbers in terms of the check digit
# 
def luhn(s):
    assert s.isdecimal()
    c = cycle((NMAP, LMAP))
    _sum = 0
    for d in s[::-1]:
        _sum += next(c)[d]
    return _sum % 10 == 0

# validates the credit card numer passed as a string

def isvalid(ccn):
    # reove any/all non-interger values
    ccn = re.sub(r'[^0-9]', '', ccn)
    # if we get a match to eny of the known expressions, validate the check digit
    for exp in MASTERCARD, VISA, DISCOVER, JCB, AMEX, DINERS, MAESTRO:
        if exp.match(ccn):
            return luhn(ccn)
    # failed to match any of the expressions
    return False
            


