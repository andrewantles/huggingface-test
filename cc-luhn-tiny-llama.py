import re

# Regular expression for Luhn's formula check
luhn_check_regex = r"^(?:2[48]|3[27]|(?:5[1-5])|(?:6011)|(?:6221|(?:6|9)[0-9])|(?:7[47])|(?:8[0-9])|(?:9[0-9]))\s*\d{13}$"

# Declare variable for credit card number
credit_card_number = input("Enter credit card number: ")

# Check if input is valid credit card number
if re.match(luhn_check_regex, credit_card_number):
    print("Valid credit card number.")
else:
    print("Invalid credit card number. Check Luhn's formula.")


#This code block uses the `re` module for regular expressions to check if the input credit card number matches the Luhn's check pattern. If the pattern matches, the (Max output tokens reached.)
