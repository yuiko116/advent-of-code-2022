with open('data.txt', 'r') as f:
    lines = f.readlines()

# A is Rock, B is paper, C is Scissors

def part2():
    dict_outcome = {
        'Z': 6, #won
        'Y': 3, #draw
        'X': 0 #lose
    }
    dict_choice = {
        'R': 1, #Rock
        'P': 2, #Paper
        'S': 3  #Scissors
    }
    total = 0
    for line in lines:
        if line[0] == 'A' and line[2] == 'Y':
            total += dict_choice['R'] + dict_outcome['Y']
        elif line[0] == 'A' and line[2] == 'Z':
            total += dict_choice['P'] + dict_outcome['Z']
        elif line[0] == 'A' and line[2] == 'X':
            total += dict_choice['S'] + dict_outcome['X']
        elif line[0] == 'B' and line[2] == 'X':
            total += dict_choice['R'] + dict_outcome['X']
        elif line[0] == 'B' and line[2] == 'Y':
            total += dict_choice['P'] + dict_outcome['Y']
        elif line[0] == 'B' and line[2] == 'Z':
            total += dict_choice['S'] + dict_outcome['Z']
        elif line[0] == 'C' and line[2] == 'X':
            total += dict_choice['P'] + dict_outcome['X']
        elif line[0] == 'C' and line[2] == 'Y':
            total += dict_choice['S'] + dict_outcome['Y']
        else:
            total += dict_choice['R'] + dict_outcome['Z']
    return total

print(part2())