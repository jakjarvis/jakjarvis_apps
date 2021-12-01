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

def error(part1_input):
    part1_solution = "Sorry, this puzzle hasn't been solved yet!"
    part2_solution = "Sorry, this puzzle hasn't been solved yet!"
    return part1_solution, part2_solution