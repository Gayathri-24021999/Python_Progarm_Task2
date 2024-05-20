# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Splitting even and odd numbers
#even = [num for num in numbers if num % 2 == 0]
#odd = [num for num in numbers if num % 2 != 0]
even = list(filter(lambda num: num %2 == 0, numbers))
odd = list(filter(lambda num: num %2 != 0, numbers))

print("Evens:", even)
print("Odds:", odd)

