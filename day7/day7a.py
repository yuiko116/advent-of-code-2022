import re
pattern = r"\d+"


def make_directory_tree():
    lines = open('d.txt', 'r')
    dir_size = {}
    current_location = ""
    current_path = []
    for line in lines:
        if line.startswith("$ cd /"):
            current_location = "/"
            current_path = ["/"]
            dir_size[current_location] = 0
        elif line.startswith("$ cd") and not line.startswith("$ cd /") and not line.startswith("$ cd .."):
            if current_location != "/":
                current_location += "/" + str(line.split(" ")[-1].strip("\n"))
            else:
                current_location += str(line.split(" ")[-1].strip("\n"))
            current_path.append(current_location.strip("\n"))
            dir_size[current_location.strip("\n")] = 0
        elif line.startswith("$ cd .."):
            current_location = "".join(current_path[-2])
            current_path.pop()
        elif line[0].isdigit():
            file_size = "".join(re.findall(pattern, line))
            for path in current_path:
                dir_size[path] += int(file_size)
    return dir_size


def calculate_total_size_below_limit():
    dir_size = make_directory_tree()
    total_size = 0
    limit = 100000

    for size in dir_size.values():
        if size <= limit:
            total_size += size

    return total_size

print(calculate_total_size_below_limit())


'''
# alternative method

with open('d.txt', 'r') as d:
    data = d.readlines()

lines = []

for line in data:
    line = re.sub('\n', '', line)
    line = line.split(" ")
    lines.append(line)


class Directory:

    def __init__(self, index, parent=None, size=0):
        self.index = index
        self.parent = parent
        self.contents = {}
        self.size = size
        self.size_below = size


root = Directory(0)
index = 1
directory_dict = {}
curr = root
for line in lines:
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                curr = curr.parent
            else:
                dirname = line[2]
                if dirname == "/":
                    curr = root
                else:
                    curr = curr.contents[dirname]
    else:
        if line[0] == "dir":
            dirname = line[1]
            directory_dict[index] = Directory(index, parent=curr)
            curr.contents[dirname] = directory_dict[index]
            index += 1
        else:
            size = int(line[0])
            filename = line[1]
            directory_dict[index] = Directory(index, parent=curr, size=size)
            curr.contents[filename] = directory_dict[index]
            index += 1

ans = 0
to_visit = [root]
visited = set()
while len(to_visit) > 0:
    directory = to_visit[-1]
    for sub in directory.contents.values():
        if sub.index not in visited:
            to_visit.append(sub)
            break
    else:
        directory = to_visit.pop()
        visited.add(directory.index)
        if directory.parent is not None:
            directory.parent.size_below += directory.size_below
        if (directory.size_below <= 100000) and (len(directory.contents) > 0):
            ans += directory.size_below

print(ans)


# dead code
# group = []
# for elem in group:
#     num = ''.join(filter(lambda i: i.isdigit(), elem))

'''