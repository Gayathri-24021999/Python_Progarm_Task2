a = [1, 1.5, 8, 26, 24]
b = [5, 24, 26, 1]
c = [10, 1, 24, 5.5, 26]

set1 = set(a)
set2 = set(b)
set3 = set(c)

duplicate = set1 & set2 & set3
duplicates_list = list(duplicate)
print(duplicates_list)

