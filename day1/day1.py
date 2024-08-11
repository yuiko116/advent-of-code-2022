
with open('puzzle_input.txt', 'r') as file:
    lines = file.readlines()

def part1():
    cal_per_elf = []
    calories = []
    for line in lines:
        if not line.isspace():
            calories.append(int(line.strip()))
            continue
        sum_of_calories = sum(calories)
        cal_per_elf.append(sum_of_calories)
        calories.clear()
    return max(cal_per_elf)

def part1_muster():
    curr_max = 0
    curr_sum = 0
    for line in lines:
        if line == "\n":
            curr_max = max(curr_sum, curr_max)
            curr_sum = 0
        else:
            curr_sum += int(line)
    return curr_max

print(part1())
print(part1_muster())



