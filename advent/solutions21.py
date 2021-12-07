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

#Day 3
def day3_2021(part1_input):
    #Part 1
    input_list = part1_input.split(' ')
    max_length = 0
    for report in input_list:
        if len(report) > max_length:
            max_length = len(report)
    gamma_rate = ""
    epsilon_rate = ""
    for digit in range(0, max_length):
        count0 = 0
        count1 = 0
        for report in input_list:
            try:
                if report[digit] == '0':
                    count0 += 1
                elif report[digit] == '1':
                    count1 += 1
                else:
                    print('Error, non-binary digit')
            except:
                pass
        if count1 > count0:
            gamma_rate += '1'
            epsilon_rate += '0'
        elif count0 > count1:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            print('Digits at ' + str(digit) + ' are tied.')
    gamma_convert = int(gamma_rate, 2)
    epsilon_convert = int(epsilon_rate, 2)
    part1_solution = gamma_convert * epsilon_convert

    #Part 2
    solution_dict = {}
    solution_dict[-1] = []
    for report in input_list:
        solution_dict[-1] += [report]
    o2gen = ""
    for digit in range(0, max_length):
        solution_dict[digit] = []
        count0 = 0
        count1 = 0
        for report in solution_dict[digit - 1]:
            try:
                if report[digit] == '0':
                    count0 += 1
                elif report[digit] == '1':
                    count1 += 1
                else:
                    print('Error, non-binary digit')
            except:
                pass
        for report in solution_dict[digit - 1]:
            if count1 >= count0:
                if report[digit] == '1':
                    solution_dict[digit] += [report]
            else:
                if report[digit] == '0':
                    solution_dict[digit] += [report]
        print(count1, count0)
        if len(solution_dict[digit]) == 1:
            o2gen = solution_dict[digit][0]
            break

    co2scrub = ""
    for digit in range(0, max_length):
        solution_dict[digit] = []
        count0 = 0
        count1 = 0
        for report in solution_dict[digit - 1]:
            try:
                if report[digit] == '0':
                    count0 += 1
                elif report[digit] == '1':
                    count1 += 1
                else:
                    print('Error, non-binary digit')
            except:
                pass
        for report in solution_dict[digit - 1]:
            if count0 <= count1:
                if report[digit] == '0':
                    solution_dict[digit] += [report]
            else:
                if report[digit] == '1':
                    solution_dict[digit] += [report]
        print(count1, count0)
        if len(solution_dict[digit]) == 1:
            co2scrub = solution_dict[digit][0]
            break
    o2_convert = int(o2gen, 2)
    co2_convert = int(co2scrub, 2)
    part2_solution = o2_convert * co2_convert

    return part1_solution, part2_solution

def error(part1_input):
    part1_solution = "Sorry, this puzzle hasn't been solved yet!"
    part2_solution = "Sorry, this puzzle hasn't been solved yet!"
    return part1_solution, part2_solution