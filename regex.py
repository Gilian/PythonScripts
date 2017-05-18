#!python3
# Projekt: Aus dem Speicher ein Telefonnummer und eine E-Mail filtern mit der Hilfe von Regex
# Steps:
# 1.) Get text of the clipboard, use pyperclip
# 2.) find all phone numbers and emails, use one regex for phone numbers and one for email, ALLE finden
# 3.) Copy it into the clipboard, schöne formatierung, text wenn es keinen eintrag gibt

import pyperclip

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))? 	# area code
	(\s|-<|\.)? 		# seperator
	(\d{3})				# first 3 digits
	(\s|-|\.)			# last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?
	)''', re.VERBOSE)

# TODO: Create email Regex

# TODO: Find matches in clipboard

# TODO: Copry results to clipboard
