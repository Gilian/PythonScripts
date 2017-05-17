# Finds a phone number with regular expressions

import re

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumberRegex.search('My number is 415-555-4242.')
print(mo.group(1))
