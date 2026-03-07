t = (10, 20, 30, 10, 40, 20)

duplicates = []

for i in range(len(t)):
    for j in range(i+1, len(t)):
        if t[i] == t[j] and t[i] not in duplicates:
            duplicates.append(t[i])

print("Duplicate elements:", duplicates)