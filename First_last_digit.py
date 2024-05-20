def sum_first_last_digit(num):
    num_str = str(num)
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    return first_digit + last_digit

# Example usage:
number = 24260102
result = sum_first_last_digit(number)
print(result)
