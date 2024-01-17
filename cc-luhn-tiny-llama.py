# Credit Card Number Validation Utility Function
def validate_credit_card(credit_card):
    # Check if credit card is valid format
    if len(credit_card)!= 16:
        print("Credit card number format error!")
        return False

    # Check if credit card digits are valid
    digits = "1234567891234567890"
    for digit in credit_card:
        if digit not in digits:
            print("Credit card number contains invalid digits!")
            return False

    return True

# Sample Credit Card Number Input
input_credit_card = "4111114117111211"

# Call validate_credit_card function with input credit card number
if validate_credit_card(input_credit_card):
    print("Credit card number is valid!")
else:
    print("Credit card number is invalid...")