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
    if any(i in check[0] for i in check[1]):
        count += 1

    # Alternative to the above if statement:
    # lst = [i for i in check[0] if i in check[1]]
    # if lst != []:
    #     count += 1

print(count)
