import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

count = 0
pattern = '\d+'

for line in lines:
    line = line.strip()
    line = line.split(',')
    check = []
    for element in line:
        num = re.findall(pattern, element)
        start = int(num[0])
        end = int(num[1])
        areas = list(range(start, end + 1))
        check.append(areas)
    if all(item in check[0] for item in check[1]) or all(item in check[1] for item in check[0]):
        print(True)
        count += 1
    else:
        print(False)

print(count)
