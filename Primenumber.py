def prime(num):
    if num<=1:
        return False
    for i in range(2, int(num ** 0.5) +1):
        if num % i ==0:
            return False
    return True

m = [10, 501, 22, 37, 100, 999, 87, 351]

prime_number = list(filter(prime, m))
print(prime_number)
