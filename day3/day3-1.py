import string

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)

with open('input.txt', 'r') as f:
    lines = f.readlines()

K = 2
score = 0

for line in lines:
    for cha in line.splitlines():
        line_len = len(cha)
        chunk_len = line_len // K
        res = []
        for c in range(0, line_len, chunk_len):
            res.append(line[c: c + chunk_len])
        pairs = []
        for item in res:
            set_item = list(set(item))
            pairs += set_item
        dup = []
        for l in pairs:
            if pairs.count(l) == 2 and l not in dup:
                dup.append(l)
            elif pairs.count(l) == 2 and l in dup:
                continue
        dup = ' '.join(dup)
        if dup in lowercase:
            score += lowercase.index(dup) + 1
        elif dup in uppercase:
            score += uppercase.index(dup) + 27

print(score)