#python credit card validator
#1. Remove any spaces or dashes from the input
#2. Add all digits in odd places from right to left
#3. Double every second digit from right to left
 #   - if the result os 2 digit number, add the 2 digit number togetherto get a single digit
#4. sum the totals of step 2 and 3
#5. if the total modulo 10 is 0, the credit card number is valid(divisible by 10)

def validate_credit_card(card_number: str) -> bool:
    # Remove spaces and dashes
    sanitized = card_number.replace(" ", "").replace("-", "")
    
    # Basic validation
    if not sanitized.isdigit():
        return False
    
    if not 13 <= len(sanitized) <= 19:
        return False
    
    total = 0
    reverse_digits = sanitized[::-1]
    
    for index, digit_char in enumerate(reverse_digits):
        digit = int(digit_char)
        
        if index % 2 == 1:  # every second digit from the right
            digit *= 2
            if digit > 9:
                digit -= 9  # equivalent to summing digits
        
        total += digit
    
    return total % 10 == 0
# Example usage
cards = validate_credit_card.card_numbers = [
    "4539 1488 0343 6467",
    "6011-1111-1111-1117",
    "378282246310005",
    "1234 5678 9012 3456"  # Invalid
]
print("Credit Card Validation Results:")
print("-------------------------------------")
for card in cards:
    is_valid = validate_credit_card(card)
    print(f"Card Number: {card} is {'valid' if is_valid else 'invalid'}")
print("-------------------------------------")
