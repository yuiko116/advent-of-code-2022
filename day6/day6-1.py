with open('d.txt', 'r') as d:
    data = d.read()

i = 0
n = 4

for fours in data:
    fours = list(data[i:n])
    if len(set(fours)) == 4:
        break
    else:
        i += 1
        n += 1

print(n)


