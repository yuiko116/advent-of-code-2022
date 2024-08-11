
with open('puzzle_input.txt', 'r') as file:
    lines = file.readlines()

def part2():
    cal_per_elf = []
    calories = []
    sum_of_top3 = 0
    for line in lines:
        if not line.isspace():
            calories.append(int(line.strip()))
            continue
        sum_of_calories = sum(calories)
        cal_per_elf.append(sum_of_calories)
        calories.clear()
    # cal_per_elf.sort(reverse=True)
    sum_of_top3 = sum(sorted(cal_per_elf)[-3:])
    return sum_of_top3

print(part2())

def part2_muster():
    sums = []
    curr_sum = 0
    for d in lines:
        if d == "\n":
            sums.append(curr_sum)
            curr_sum = 0
        else:
            curr_sum += int(d)

    return sum(sorted(sums)[-3:])

print(part2_muster())

