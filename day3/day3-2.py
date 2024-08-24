import string

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)

with open('input.txt', 'r') as f:
    lines = f.readlines()

score = 0
count = 0
group = []

for line in lines:
    count += 1
    line = ' '.join(line.split())
    line = list(set(line))
    group += line
    if count == 3:
        dup = []
        for l in group:
            if group.count(l) == 3 and l not in dup:
                dup.append(l)
        dup = ' '.join(dup)
        if dup in lowercase:
            score += lowercase.index(dup) + 1
        elif dup in uppercase:
            score += uppercase.index(dup) + 27
        group.clear()
        count = 0

print(score)