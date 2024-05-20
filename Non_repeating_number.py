a = [1, 1.5, 8, 26, 24, 26, 24]
count = Counter(a)
non_repeating_numbers = [num for num, cnt in count.items() if cnt == 1]
print(non_repeating_numbers)
