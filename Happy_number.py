def happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(x) ** 2 for x in str(num))
    return num == 1

numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Filtering happy numbers
happy_numbers = list(filter(happy, numbers))

print("Happy Numbers:", happy_numbers)
