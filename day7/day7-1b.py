
def add_path_to_directories(path, directories):
    if path not in directories.keys():
        directories[path] = 0
    return directories


def solution():
    f = open('d.txt', 'r')
    directories_size = {}
    current_stack = []
    current_path = ""
    for line in f:
        if line.startswith("$ cd"):
            if not line.startswith("$ cd ..") and not line.startswith("$ cd /"):
                current_path += f"/{line.split()[-1]}" if current_path != "/" else line.split()[-1]
                print(current_path)
                current_stack.append(current_path)
                directories_size = add_path_to_directories(current_path, directories_size)

            elif line.strip() == "$ cd /":
                current_path = "/"
                print(current_path)
                current_stack = ["/"]
                directories_size = add_path_to_directories(current_path, directories_size)

            elif line.strip() == "$ cd ..":
                print(current_path)
                current_path = "/".join(current_path.split("/")[:-1])
                print(current_path)
                print(current_stack)
                current_stack.pop()
                print(current_stack)

        if line[0].isdigit():
            file_size = int(line.split()[0])
            for directory in current_stack:
                directories_size[directory] += file_size

    final_list_task_1 = [el for el in directories_size.values() if el <= 100000]
    print("Task 1:")
    print(sum(final_list_task_1))
    print(directories_size)

print(solution())