import re

def is_valid_credit_card(card_number):
   
    if not re.match(r"^[456]\d{3}(-?\d{4}){3}$", card_number):
        return "Invalid"

   
    card_number_no_hyphen = card_number.replace("-", "")

   
    if not card_number_no_hyphen.isdigit():
        return "Invalid"


    if len(card_number_no_hyphen) != 16:
        return "Invalid"

  
    if re.search(r"(\d)\1{3,}", card_number_no_hyphen):
        return "Invalid"

    return "Valid"


n = int(input().strip())
for _ in range(n):
    card_number = input().strip()
    print(is_valid_credit_card(card_number))
