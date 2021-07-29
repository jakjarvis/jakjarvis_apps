def solution(year, day, part1_input, part2_input):

    def day1_2015(part1_input):
        #Part 1
        counter = 0
        for a in part1_input:
            if a == "(":
                counter += 1
            elif a == ")":
                counter -= 1
            else:
                break
                print("Error")
        solution1 = counter

        #Part 2
        counter = 0
        position = 0
        for a in part1_input:
            if a == "(":
                counter += 1
            elif a == ")":
                counter -= 1
            else:
                break
                print("Error")
            position += 1
            if counter <= -1:
                break
        solution2 = position

        return solution1, solution2

    def day2_2015(part1_input):

        #Part 1
        input_list = part1_input.split()
        areas_list = []
        order_list = []
        shopping_list = []

        for present in input_list:
            a, b, c = present.split('x')
            areas_list.append([int(a), int(b), int(c)])

        for a in areas_list:
            x = 2 * a[0] * a[1]
            y = 2 * a[1] * a[2]
            z = 2 * a[2] * a[0]
            b = [x, y, z]
            b.sort()
            xtra = b[:1]
            b.append(xtra[0] / 2)
            order_list.append(b)

        for present in order_list:
            shopping_list.append(sum(present))

        solution1 = sum(shopping_list)

        print(input_list)

        #Part 2
        ribbon_list = []
        for a in areas_list:
            a.sort()
            ribbon = 2 * a[0] + 2 * a[1] + (a[0] * a[1] * a[2])
            ribbon_list.append(ribbon)
        solution2 = sum(ribbon_list)

        return solution1, solution2

    def day3_2015(part1_input):
        #Part 1
        Visits = [[0, 0]]
        Coord = [0, 0]
        print(part1_input)
        for char in part1_input:
            x = char
            if x == "^":
                Coord[0] = Coord[0] + 1
                Visits.append(Coord.copy())
            elif x == "v":
                Coord[0] = Coord[0] - 1
                Visits.append(Coord.copy())
            elif x == "<":
                Coord[1] = Coord[1] - 1
                Visits.append(Coord.copy())
            elif x == ">":
                Coord[1] = Coord[1] + 1
                Visits.append(Coord.copy())

        Unique_Houses = []
        for item in Visits:
            if item not in Unique_Houses:
                Unique_Houses.append(item)

        solution1 = len(Unique_Houses)
        #solution1 = part1_input

        #Part 2
        Coord1 = [0, 0]
        Coord2 = [0, 0]
        Counter = 1
        Stops = [[0, 0]]

        for char in part1_input:
            x = char
            if x == "^":
                if Counter == 1:
                    Coord1[0] = Coord1[0] + 1
                    Stops.append(Coord1.copy())
                    Counter = 2
                else:
                    Coord2[0] = Coord2[0] + 1
                    Stops.append(Coord2.copy())
                    Counter = 1
            elif x == "v":
                if Counter == 1:
                    Coord1[0] = Coord1[0] - 1
                    Stops.append(Coord1.copy())
                    Counter = 2
                else:
                    Coord2[0] = Coord2[0] - 1
                    Stops.append(Coord2.copy())
                    Counter = 1
            elif x == "<":
                if Counter == 1:
                    Coord1[1] = Coord1[1] - 1
                    Stops.append(Coord1.copy())
                    Counter = 2
                else:
                    Coord2[1] = Coord2[1] - 1
                    Stops.append(Coord2.copy())
                    Counter = 1
            elif x == ">":
                if Counter == 1:
                    Coord1[1] = Coord1[1] + 1
                    Stops.append(Coord1.copy())
                    Counter = 2
                else:
                    Coord2[1] = Coord2[1] + 1
                    Stops.append(Coord2.copy())
                    Counter = 1

        Unique_Stops = []
        for item in Stops:
            if item not in Unique_Stops:
                Unique_Stops.append(item)

        solution2 = len(Unique_Stops)

        return solution1, solution2

    # Match solution to function
    if year == "2015" and day == "1":
        solution1, solution2 = day1_2015(part1_input)
    if year == "2015" and day == "2":
        solution1, solution2 = day2_2015(part1_input)
    if year == "2015" and day == "3":
        solution1, solution2 = day3_2015(part1_input)

    return solution1, solution2