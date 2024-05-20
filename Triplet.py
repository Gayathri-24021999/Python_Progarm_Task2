def triplet(s, target):
    n = len(s)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if s[i] + s[j]+ s[k] == target:
                    return [s[i], s[j], s[k]]
    return None

s = [10,20,30,9]
target = 59
triplet = triplet(s, target)

if triplet:
    print("Triplet found:", triplet)
else:
    print("No triplet found with the given target value.")
