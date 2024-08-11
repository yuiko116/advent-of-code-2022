
with open('data.txt', 'r') as f:
    lines = f.readlines()

# A is Rock, B is paper, C is Scissors

def part1():
    dict_result = {
        'won': 6,
        'draw': 3,
        'lost': 0
    }
    dict_choice = {
        'X': 1, #Rock
        'Y': 2, #Paper
        'Z': 3  #Scissors
    }
    total = 0
    for line in lines:
        if line[0] == 'A' and line[2] == 'Y':
            total += dict_result['won'] + dict_choice['Y']
        elif line[0] == 'A' and line[2] == 'Z':
            total += dict_result['lost'] + dict_choice['Z']
        elif line[0] == 'A' and line[2] == 'X':
            total += dict_result['draw'] + dict_choice['X']
        elif line[0] == 'B' and line[2] == 'X':
            total += dict_result['lost'] + dict_choice['X']
        elif line[0] == 'B' and line[2] == 'Y':
            total += dict_result['draw'] + dict_choice['Y']
        elif line[0] == 'B' and line[2] == 'Z':
            total += dict_result['won'] + dict_choice['Z']
        elif line[0] == 'C' and line[2] == 'X':
            total += dict_result['won'] + dict_choice['X']
        elif line[0] == 'C' and line[2] == 'Y':
            total += dict_result['lost'] + dict_choice['Y']
        else:
            total += dict_result['draw'] + dict_choice['Z']
    return total

print(part1())

