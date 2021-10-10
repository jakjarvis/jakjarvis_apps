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

def day4_2016(part1_input):
    import pandas as pd

    part1_input = part1_input.decode("utf-8")  # the file reads in as a bytes (b') type - need to convert it to string type

    def check_room(room):
        room_parts = room.split('-')
        id_check = room_parts[-1][:-1]
        room_parts = room_parts[:-1]
        room_parts += id_check.split('[')

        number = room_parts[-2]

        room_name = ''
        for name_part in room_parts[:-2]:
            room_name += name_part
        letter_count = {}
        for character in room_name:
            if character in letter_count:
                letter_count[character] += 1
            else:
                letter_count[character] = 1

        letter_frame = pd.DataFrame(letter_count.items(), index=range(len(letter_count)))
        letter_frame = letter_frame.sort_values([1, 0], ascending=[False, True])
        true_checksum = ''.join(letter_frame[0][:5].values.tolist())

        valid = False
        if room_parts[-1] == true_checksum:
            valid = True

        # Part 2
        real_name = ''
        for character in room_name:
            letter_ord = ord(character)
            letter_ord += int(number) % 26
            if letter_ord >= (96 + 27):
                letter_ord -= 26
            real_name += chr(letter_ord)
        print(real_name)
        right_room = False
        if real_name == 'northpoleobjectstorage':
            right_room = True

        return valid, number, right_room

    def solver(part1_input):
        input_list = []
        character = 0
        while len(part1_input) != 0:
            if part1_input[character] == ']':
                input_list += [part1_input[:character + 1].replace("\n", "").replace("\r", "")]
                part1_input = part1_input[character + 1:]
                character = 0
            else:
                character += 1
        print(input_list)

        part1_solution = 0
        part2_solution = 0
        for room in input_list:
            valid, number, right_room = check_room(room)
            if valid == True:
                part1_solution += int(number)
            if right_room == True:
                part2_solution = number

        return part1_solution, part2_solution

    part1_solution, part2_solution = solver(part1_input)
    return part1_solution, part2_solution

def day5_2016(part1_input):
    import hashlib
    import collections
    index = 0
    part1_solution = ''
    password_dict = {}
    while len(password_dict) <= 7:
        key = part1_input + str(index)
        hashed_key = hashlib.md5(bytes(key, encoding='utf-8')).hexdigest()
        if hashed_key[:5] == '00000':
            if len(part1_solution) <= 7:
                part1_solution += hashed_key[5]
            if hashed_key[5] in ['0', '1', '2', '3', '4', '5', '6', '7']:
                if hashed_key[5] not in password_dict.keys():
                    location = hashed_key[5]
                    value = hashed_key[6]
                    password_dict[location] = value
        index += 1
        if index % 1000000 == 0:
            print(index)

    od = collections.OrderedDict(sorted(password_dict.items()))
    part2_solution = ''
    for value in od.values():
        part2_solution += value

    return part1_solution, part2_solution