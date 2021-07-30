def solution(year, day, part1_input, part2_input):

#Day 1
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

#Day 2
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

#Day 3
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

#Day 4
    def day4_2015(part1_input):
        import hashlib

        #Part 1
        key = part1_input
        counter = 1
        concat = key + str(counter)
        code = hashlib.md5(concat.encode('utf-8'))

        while str(code.hexdigest())[0:5] != '00000':
            counter = counter + 1
            concat = key + str(counter)
            code = hashlib.md5(concat.encode('utf-8'))

        solution1 = counter

        #Part 2
        key = part1_input
        counter = 1
        concat = key + str(counter)
        code = hashlib.md5(concat.encode('utf-8'))

        while str(code.hexdigest())[0:6] != '000000':
            counter = counter + 1
            concat = key + str(counter)
            code = hashlib.md5(concat.encode('utf-8'))

        solution2 = counter

        return solution1, solution2

#Day 5
    def day5_2015(part1_input):
        input_list = part1_input.split()

        def countvowels(word):
            vowels = False
            a = word.count('a')
            e = word.count('e')
            i = word.count('i')
            o = word.count('o')
            u = word.count('u')
            if (a + e + i + o + u) >= 3:
                vowels = True
            else:
                vowels = False
            return vowels


        def countdups(word):
            counter = 0
            dups = False
            a = ''
            for char in word:
                if char == a:
                    dups = True
                a = char
            return dups


        def checksubs(word):
            subs = False
            if "ab" in word or "cd" in word or "pq" in word or "xy" in word:
                subs = True
            return subs

        counter = 0

        for entry in input_list:
            vowels = countvowels(entry)
            dups = countdups(entry)
            subs = checksubs(entry)

            # If all tests are good, increase the counter
            if vowels == True and dups == True and subs == False:
                counter = counter + 1

        solution1 = counter

        #Part 2
        def doublepair(word):
            n = len(word)
            c = len(word)
            dubs = False
            for a in word:
                pair = a + word[(1 + n - c)]
                b = word.count(pair)
                trip = a + a + a
                d = word.count(trip)
                quad = a + a + a + a
                p = word.count(quad)
                if p >= 1 or b - d >= 2:
                    dubs = True
                    break
                c = c - 1
                if c <= 1:
                    break
            return dubs

        def bridge(word):
            n = 2
            l = len(word)
            xyx = False
            for a in word:
                if a == word[n]:
                    xyx = True
                    break
                n = n + 1
                if n == l:
                    break
            return xyx

        counter = 0
        for entry in input_list:
            dubs = doublepair(entry)
            xyx = bridge(entry)
            if dubs == True and xyx == True:
                counter = counter + 1

        solution2 = counter

        return solution1, solution2

#Day 6
    def day6_2015(part1_input):
        import numpy as np

        #Part 1
        grid = np.zeros((1000, 1000))
        split_input = part1_input.split()
        input_list = []
        counter = 1
        for word in split_input[1:]:
            if word == 'turn' or word == 'toggle':
                input_list += [' '.join(split_input[:counter])]
                split_input = split_input[counter:]
                counter = 0
            counter += 1
        input_list += [' '.join(split_input)]

        def turnoff(command, grid):
            start = command.split(' ')[2]
            startx = int(start.split(',')[0])
            starty = int(start.split(',')[1])
            end = command.split(' ')[4]
            endx = int(end.split(',')[0]) + 1
            endy = int(end.split(',')[1]) + 1

            counterx = startx
            countery = starty
            changed = 0

            for x in grid[startx:endx]:
                for y in x[starty:endy]:
                    grid[counterx, countery] = 0
                    countery += 1
                    changed += 1
                countery = starty
                counterx += 1
            return grid


        def turnon(command, grid):
            start = command.split(' ')[2]
            startx = int(start.split(',')[0])
            starty = int(start.split(',')[1])
            end = command.split(' ')[4]
            endx = int(end.split(',')[0]) + 1
            endy = int(end.split(',')[1]) + 1

            counterx = startx
            countery = starty
            changed = 0

            for x in grid[startx:endx]:
                for y in x[starty:endy]:
                    grid[counterx, countery] = 1
                    countery += 1
                    changed += 1
                countery = starty
                counterx += 1
            return grid


        def toggle(command, grid):
            start = command.split(' ')[1]
            startx = int(start.split(',')[0])
            starty = int(start.split(',')[1])
            end = command.split(' ')[3]
            endx = int(end.split(',')[0]) + 1
            endy = int(end.split(',')[1]) + 1

            counterx = startx
            countery = starty
            changed = 0

            for x in grid[startx:endx]:
                for y in x[starty:endy]:
                    if y == 1:
                        grid[counterx, countery] -= 1
                    else:
                        grid[counterx, countery] += 1
                    countery += 1
                    changed += 1
                countery = starty
                counterx += 1
            return grid

        for command in input_list:
            if command.split(' ')[0] == 'toggle':
                grid = toggle(command, grid)
            elif command.split(' ')[1] == 'off':
                grid = turnoff(command, grid)
            elif command.split(' ')[1] == 'on':
                grid = turnon(command, grid)
            else:
                print('Command Error')

        solution1 = np.sum(grid)

        #Part 2
        grid = np.zeros((1000, 1000))

        def turnoff2(command, grid):
            start = command.split(' ')[2]
            startx = int(start.split(',')[0])
            starty = int(start.split(',')[1])
            end = command.split(' ')[4]
            endx = int(end.split(',')[0]) + 1
            endy = int(end.split(',')[1]) + 1

            counterx = startx
            countery = starty
            changed = 0

            for x in grid[startx:endx]:
                for y in x[starty:endy]:
                    if y >= 1:
                        grid[counterx, countery] -= 1
                    countery += 1
                    changed += 1
                countery = starty
                counterx += 1
            return grid

        def turnon2(command, grid):
            start = command.split(' ')[2]
            startx = int(start.split(',')[0])
            starty = int(start.split(',')[1])
            end = command.split(' ')[4]
            endx = int(end.split(',')[0]) + 1
            endy = int(end.split(',')[1]) + 1

            counterx = startx
            countery = starty
            changed = 0

            for x in grid[startx:endx]:
                for y in x[starty:endy]:
                    grid[counterx, countery] += 1
                    countery += 1
                    changed += 1
                countery = starty
                counterx += 1
            return grid

        def toggle2(command, grid):
            start = command.split(' ')[1]
            startx = int(start.split(',')[0])
            starty = int(start.split(',')[1])
            end = command.split(' ')[3]
            endx = int(end.split(',')[0]) + 1
            endy = int(end.split(',')[1]) + 1

            counterx = startx
            countery = starty
            changed = 0

            for x in grid[startx:endx]:
                for y in x[starty:endy]:
                    grid[counterx, countery] += 2
                    countery += 1
                    changed += 1
                countery = starty
                counterx += 1
            return grid

        for command in input_list:
            if command.split(' ')[0] == 'toggle':
                toggle2(command, grid)
            elif command.split(' ')[1] == 'off':
                turnoff2(command, grid)
            elif command.split(' ')[1] == 'on':
                turnon2(command, grid)
            else:
                print('Command Error')

        solution2 = np.sum(grid)

        return solution1, solution2

#Day 7
    def day7_2015(part1_input):
        split_input = part1_input.split()
        input_list = []
        counter = 0
        while counter < len(split_input):
            if split_input[counter] == '->':
                input_list += [' '.join(split_input[:(counter + 2)])]
                split_input = split_input[(counter + 2):]
                counter = 0
            else:
                counter += 1

        # Part 1
        def run(input_list, signals, count):
            count = 0
            for step in input_list:
                split = str.split(step)
                if 'NOT' in split:
                    signals, count = NOTGate(step, signals, count)
                elif 'OR' in split:
                    signals, count = ORGate(step, signals, count)
                elif 'AND' in split:
                    signals, count = ANDGate(step, signals, count)
                elif 'RSHIFT' in split:
                    signals, count = RSGate(step, signals, count)
                elif 'LSHIFT' in split:
                    signals, count = LSGate(step, signals, count)
                elif '->' in split:
                    signals, count = noGate(step, signals, count)
                else:
                    raise Exception('Unrecognised input.')

            return signals, count


        def noGate(step, dic, exc):
            list = str.split(step)
            try:
                list[0] = int(list[0])
            except:
                pass

            if list[2] not in dic:
                if isinstance(list[0], int) == True:
                    dic[list[2]] = list[0]
                elif list[0] in dic:
                    dic[list[2]] = dic[list[0]]
                else:
                    exc = exc + 1
            return dic, exc

        def NOTGate(step, dic, exc):
            list = str.split(step)  # splits into a list containing [NOT, ll, ->, ll]
            try:
                list[1] = int(list[1])
            except:
                pass

            if list[3] not in dic:
                if isinstance(list[1], int) == True:
                    newSignal = ~(list[1])
                    dic[list[3]] = newSignal
                elif list[1] in dic:
                    newSignal = ~(dic[list[1]])
                    dic[list[3]] = newSignal
                else:
                    exc = exc + 1
            return dic, exc

        def ORGate(step, dic, exc):
            list = str.split(step)  # splits into a list containing [ll, OR, ll, ->, ll]
            try:
                list[0] = int(list[0])
            except:
                pass
            try:
                list[2] = int(list[2])
            except:
                pass

            if list[4] not in dic:
                if isinstance(list[0], int) and isinstance(list[2], int) == True:
                    newSignal = (list[0] | list[2])
                    dic[list[4]] = newSignal
                elif isinstance(list[0], int) == True and list[2] in dic:
                    newSignal = (list[0] | dic[list[2]])
                    dic[list[4]] = newSignal
                elif isinstance(list[2], int) == True and list[0] in dic:
                    newSignal = (dic[list[0]] | list[2])
                    dic[list[4]] = newSignal
                elif list[0] in dic:
                    if isinstance(list[2], int) == True:
                        newSignal = (dic[list[0]] | list[2])
                        dic[list[4]] = newSignal
                    elif list[2] in dic:
                        print(list[0], list[2])
                        newSignal = (dic[list[0]] | dic[list[2]])
                        dic[list[4]] = newSignal
                else:
                    exc = exc + 1
            return dic, exc

        def ANDGate(step, dic, exc):
            list = str.split(step)
            try:
                list[0] = int(list[0])
            except:
                pass
            try:
                list[2] = int(list[2])
            except:
                pass

            if list[4] not in dic:
                if isinstance(list[0], int) and isinstance(list[2], int) == True:
                    newSignal = (list[0] & list[2])
                    dic[list[4]] = newSignal
                elif isinstance(list[0], int) == True and list[2] in dic:
                    newSignal = (list[0] & dic[list[2]])
                    dic[list[4]] = newSignal
                elif list[0] in dic:
                    if isinstance(list[2], int) == True:
                        newSignal = (dic[list[0]] & list[2])
                        dic[list[4]] = newSignal
                    elif list[2] in dic:
                        print(list[0], list[2])
                        newSignal = (dic[list[0]] & dic[list[2]])
                        dic[list[4]] = newSignal
                else:
                    exc = exc + 1
            return dic, exc

        def RSGate(step, dic, exc):
            list = str.split(step)

            if list[4] not in dic:
                if list[0] in dic:
                    newSignal = (dic[list[0]] >> int(list[2]))
                    dic[list[4]] = newSignal
                else:
                    exc = exc + 1
            return dic, exc

        def LSGate(step, dic, exc):
            list = str.split(step)

            if list[4] not in dic:
                if list[0] in dic:
                    newSignal = (dic[list[0]] << int(list[2]))
                    dic[list[4]] = newSignal
                else:
                    exc = exc + 1
            return dic, exc

        signals = {}
        counter = 1
        while counter != 0:
            signals, counter = run(input_list, signals, counter)
        solution1 = signals['a']

        #Part 2

        counter = 0
        while counter < len(input_list):
            if input_list[counter][-2:] == ' b':
                input_list[counter] = str(signals['a']) + ' -> b'
            counter += 1

        signals = {}
        counter = 1
        while counter != 0:
            signals, counter = run(input_list, signals, counter)
        solution2 = signals['a']

        return solution1, solution2

#Day 8
    def day8_2015(part1_input):

        input_list = list(part1_input)
        # This is a really lazy bit of refactoring to just force the import to match what Jupyter notebooks would read :p
        for char in range(0,len(input_list)):
            if input_list[char] == ' ':
                input_list[char] = '\n'

        #Part 1
        codeCount = 0
        strCount = 0
        holdTag = 0

        for char in input_list:

            if holdTag == 3:  # ignores the second hex character
                holdTag = 0

            elif holdTag == 2:  # ignores the first hex character
                holdTag = 3

            elif holdTag == 1:
                if char == '"':  # ignores the extra \
                    holdTag = 0
                elif char == '\\':  # ignores the extra \
                    holdTag = 0
                elif char == 'x':  # ignores the extra \
                    holdTag = 2

            elif char == '\\':  # counts one for any escape sequence, then enters loop to ignore the rest
                holdTag = 1
                strCount = strCount + 1

            elif char == '\n':  #
                codeCount -= 1

            elif char == '"':
                pass

            else:
                strCount = strCount + 1

            codeCount += 1
        solution1 = codeCount - strCount

        #Part 2

        codeCount = 0
        encodeCount = 2  # start at two to cover the additional " you'll need at either end

        for char in input_list:

            if char == '"':
                encodeCount += 2

            elif char == '\\':
                encodeCount += 2

            elif char == '\n':  #
                codeCount -= 1
                encodeCount += 2  # to add the " to the end of the current expression and the start of the new one

            else:
                encodeCount += 1

            codeCount += 1

            solution2 = encodeCount - codeCount

        return solution1, solution2

# Match solution to function
    if year == "2015":
        if day == "1": solution1, solution2 = day1_2015(part1_input)
        if day == "2": solution1, solution2 = day2_2015(part1_input)
        if day == "3": solution1, solution2 = day3_2015(part1_input)
        if day == "4": solution1, solution2 = day4_2015(part1_input)
        if day == "5": solution1, solution2 = day5_2015(part1_input)
        if day == "6": solution1, solution2 = day6_2015(part1_input)
        if day == "7": solution1, solution2 = day7_2015(part1_input)
        if day == "8": solution1, solution2 = day8_2015(part1_input)

    return solution1, solution2