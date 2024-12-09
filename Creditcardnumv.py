import time

print("-----------Credit-Card-Number-Validator------------")
while True:
    card_num = input("Insert the Credit Card Number: ").replace("-", "").replace(" ", "")
    
    if card_num.isdigit() and len(card_num) >= 13:
        break
    else:
        print("Invalid input. Please enter only numeric digits, with optional spaces or dashes.")


rev_card_num = card_num[::-1]
sum_digits = 0
final_digits = []

for char in rev_card_num[1::2]:
    doubled_digit = int(char)*2
    if doubled_digit > 9:
        doubled_digit = doubled_digit - 9
        final_digits.append(doubled_digit)
    else:
        final_digits.append(doubled_digit)

for num in rev_card_num[::2]:
    sum_digits += int(num)

sum_digits += sum(final_digits)

if sum_digits % 10 == 0:
    print("Checking---")
    time.sleep(0.5)
    print("It's a valid credit card number.")
    print("---------------------------------------------------")
else:
    print("Checking---")
    time.sleep(0.5)
    print("Invalid credit card number.")
    print("---------------------------------------------------")