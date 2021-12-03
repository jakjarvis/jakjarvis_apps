#Day 1
def day1_2021(part1_input):

    input_list = list(map(int, part1_input.split(' ')))

    part1_solution = 0
    for scan in range(1, len(input_list)):
        if input_list[scan] > input_list[scan - 1]:
            part1_solution += 1

    part2_solution = 0
    for scan in range(3, len(input_list)):
        if (input_list[scan] + input_list[scan - 1] + input_list[scan - 2]) > (
                input_list[scan - 1] + input_list[scan - 2] + input_list[scan - 3]):
            part2_solution += 1

    return part1_solution, part2_solution

#Day 2
def day2_2021(part1_input):
    input_list = part1_input.split(' ')
    depth = 0
    distance = 0
    for direction in range(0, len(input_list), 2):
        if input_list[direction] == 'forward':
            distance += int(input_list[direction + 1])
        elif input_list[direction] == 'down':
            depth += int(input_list[direction + 1])
        elif input_list[direction] == 'up':
            depth -= int(input_list[direction + 1])
        else:
            print('Incorrect direction entered')
    part1_solution = depth * distance

    aim = 0
    depth = 0
    distance = 0
    for direction in range(0, len(input_list), 2):
        if input_list[direction] == 'forward':
            distance += int(input_list[direction + 1])
            depth += aim * int(input_list[direction + 1])
        elif input_list[direction] == 'down':
            aim += int(input_list[direction + 1])
        elif input_list[direction] == 'up':
            aim -= int(input_list[direction + 1])
        else:
            print('Incorrect direction entered')
    part2_solution = depth * distance

    return part1_solution, part2_solution

def error(part1_input):
    part1_solution = "Sorry, this puzzle hasn't been solved yet!"
    part2_solution = "Sorry, this puzzle hasn't been solved yet!"
    return part1_solution, part2_solution