from day7a import make_directory_tree


def find_cleaning():
    dir_size = make_directory_tree()
    size_root = dir_size['/']
    max_space = 70000000
    need_for_update = 30000000
    current_free_space = max_space - size_root
    to_be_cleaned = need_for_update - current_free_space
    answer = sorted([el for el in dir_size.values() if el >= to_be_cleaned])
    return min(answer)

print(find_cleaning())