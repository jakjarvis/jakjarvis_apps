# Day 1
def day1_2016(part1_input):
    # Set up variables
    directions = part1_input.split(', ')
    direction = 'N'
    longitude = 0
    latitude = 0
    visited_places = [(0, 0)]
    part2_solution = None
    # For each step in the instructions, check if left or right and update the direction
    for step in directions:
        if step[0] == 'L':
            if direction == 'N':
                direction = 'W'
            elif direction == 'E':
                direction = 'N'
            elif direction == 'S':
                direction = 'E'
            elif direction == 'W':
                direction = 'S'
            else:
                print('Incorrect direction recorded')
                break
        elif step[0] == 'R':
            if direction == 'N':
                direction = 'E'
            elif direction == 'E':
                direction = 'S'
            elif direction == 'S':
                direction = 'W'
            elif direction == 'W':
                direction = 'N'
            else:
                print('Incorrect direction recorded')
                break
        else:
            print('Incorrect instruction provided')
            break

        # If part 2 is not yet solved, add all waypoints to the visited_places
        # and check if they are a repeat, if so, set the part2 solution
        for block in range(1, int(step[1:]) + 1):
            if direction == 'N':
                location = (longitude + block, latitude)
            elif direction == 'E':
                location = (longitude, latitude + block)
            elif direction == 'S':
                location = (longitude - block, latitude)
            elif direction == 'W':
                location = (longitude, latitude - block)

            if part2_solution == None:
                if location in visited_places:
                    part2_coordinates = location
                    part2_solution = abs(part2_coordinates[0]) + abs(part2_coordinates[1])
                else:
                    visited_places += [location]

        # Update the current coordinates after the instruction is complete
        longitude = location[0]
        latitude = location[1]

    part1_solution = abs(latitude) + abs(longitude)

    return part1_solution, part2_solution

# Day 2
def day2_2016(part1_input):
    input_list = part1_input.split(' ')

    def buttons(keypad, key):
        commands = []
        for sequence in input_list:
            for step in sequence:
                if step == 'U':
                    if keypad[key[0] - 1][key[1]] != None:
                        key[0] -= 1
                elif step == 'D':
                    if keypad[key[0] + 1][key[1]] != None:
                        key[0] += 1
                elif step == 'L':
                    if keypad[key[0]][key[1] - 1] != None:
                        key[1] -= 1
                elif step == 'R':
                    if keypad[key[0]][key[1] + 1] != None:
                        key[1] += 1
                else:
                    print('Incorrect instruction')
            commands += [str(keypad[key[0]][key[1]])]
        return ''.join(commands)

    keypad_1 = [[None, None, None, None, None],
                [None, 1, 2, 3, None],
                [None, 4, 5, 6, None],
                [None, 7, 8, 9, None],
                [None, None, None, None, None]]
    key_1 = [2, 2]
    part1_solution = buttons(keypad_1, key_1)

    keypad_2 = [[None, None, None, None, None, None, None],
                [None, None, None, 1, None, None, None],
                [None, None, 2, 3, 4, None, None],
                [None, 5, 6, 7, 8, 9, None],
                [None, None, 'A', 'B', 'C', None, None],
                [None, None, None, 'D', None, None, None],
                [None, None, None, None, None, None, None]]
    key_2 = [3, 1]
    part2_solution = buttons(keypad_2, key_2)

    return part1_solution, part2_solution

# Day 3
def day3_2016(part1_input):
    # Transform input into list of lists of integers
    split_input = part1_input.split(' ')
    while '' in split_input:
        split_input.remove('')
    input_list = []
    while len(split_input) > 0:
        side_list_str = split_input[:3]
        split_input = split_input[3:]
        side_list_int = []
        for side in side_list_str:
            side_list_int += [int(side)]
        input_list += [side_list_int]
    # Count number of valid triangles in list
    total_triangles = len(input_list)
    invalid_triangles = 0
    for triangle in input_list:
        if triangle[0] + triangle[1] <= triangle[2] or triangle[0] + triangle[2] <= triangle[1] or triangle[1] + \
                triangle[2] <= triangle[0]:
            invalid_triangles += 1
    solution1 = total_triangles - invalid_triangles
    # For Part 2, use every third triangle as a set
    invalid_triangles = 0
    while len(input_list) > 0:
        group_of_3 = input_list[:3]
        for column in range(3):
            if group_of_3[0][column] + group_of_3[1][column] <= group_of_3[2][column] or group_of_3[0][column] + \
                    group_of_3[2][column] <= group_of_3[1][column] or group_of_3[1][column] + group_of_3[2][column] <= \
                    group_of_3[0][column]:
                invalid_triangles += 1
        input_list = input_list[3:]
        solution2 = total_triangles - invalid_triangles

    return solution1, solution2