import numpy as np
import re

with open('a.txt', 'r') as a:
    lines = a.readlines()

with open('b.txt', 'r') as b:
    orders = b.readlines()

m = []
n = 4

for line in lines[:-1]:
    line = re.sub('\n', '', line)
    result = [line[i:i + n] for i in range(0, len(line), n)]
    m.append(result)

m = np.array(m)
m = m.transpose()
m_list = m.tolist()

new_list = []

for i in m_list:
    i = re.sub(r'[\[\]\s]', '', str(i))
    l = []
    for e in i:
        match = re.search(r'\w', str(e))
        if match:
            l.append(e)
    l.reverse()
    new_list.append(l)

o = []
for order in orders:
    order = re.findall(r'\d+', order)
    o.append(order)

for num in o:
    pieces = int(num[0])
    origin = int(num[1])
    goal = int(num[2])
    appended_to = new_list[goal-1]
    to_append = new_list[origin-1][len(new_list[origin-1])-pieces:]
    to_be_moved = to_append[::-1]
    new_pile = appended_to + to_be_moved
    new_list[goal - 1] = new_pile
    del new_list[origin - 1][-pieces:]

message = []
for item in new_list:
    message.append(item[-1])

message = re.sub(r'[\[\]\s]', '', str(message))
message = re.findall(r'\w', str(message))
message = ''.join(message)
print(message)
