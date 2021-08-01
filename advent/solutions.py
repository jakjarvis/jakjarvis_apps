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

#Day 9
    def day9_2015(part1_input):
        import itertools

        split_input = part1_input.split()
        input_list = []
        counter = 0
        while len(split_input) > 0:
            try:
                a = int(split_input[counter])
                input_list += [' '.join(split_input[:(counter + 1)])]
                split_input = split_input[(counter + 1):]
                counter = 0
            except:
                counter += 1

        #Part 1
        places = []
        for route in input_list:
            step = str.split(route)
            if step[0] in places:
                pass
            else:
                places += [step[0]]
            if step[2] in places:
                pass
            else:
                places += [step[2]]

        register = {}

        for place in places:
            otherPlaces = places.copy()
            otherPlaces.remove(place)
            register[place] = {}
            for otherPlace in otherPlaces:
                for route in input_list:
                    step = str.split(route)
                    if place in step and otherPlace in step:
                        register[place][otherPlace] = int(step[4])

        answer = 1000000
        for combo in list(itertools.permutations(places)):
            length = len(combo)
            step = 0
            total = 0
            for leg in combo:
                if step == length - 1:
                    pass
                else:
                    total += register[combo[step]][combo[step + 1]]
                step += 1

            if total <= answer:
                answer = total
        solution1 = answer

        #Part 2
        answer = 0
        for combo in list(itertools.permutations(places)):
            length = len(combo)
            step = 0
            total = 0
            for leg in combo:
                if step == length - 1:
                    pass
                else:
                    total += register[combo[step]][combo[step + 1]]
                step += 1

            if total >= answer:
                answer = total
        solution2 = answer

        return solution1, solution2

#Day 10
    def day10_2015(part1_input):

        #Part 1
        LaS = part1_input
        for n in range(40):
            new = ""
            counter = 1
            run = 1
            for x in LaS:
                if counter == len(LaS):
                    new = new + str(run) + str(x)
                    LaS = new

                elif x == LaS[counter]:
                    run += 1

                else:
                    new = new + str(run) + str(x)
                    run = 1

                counter += 1
            solution1 = str(len(LaS))

        #Part 2

        solution2 = "Due to server constraints, Part 2 must be run on a local machine. Code can be accessed through the 'solution' link:"

        return solution1, solution2

#Day 11
    def day11_2015(part1_input):

        def solution(inpt):
            numInpt = []
            oupt = ''

            for char in inpt:
                number = ord(char) - 96
                numInpt.append(number)

            run = False
            trick = False
            pair1 = False
            pair2 = False
            counter3 = 0

            for x in range(1000000):

                run = False
                trick = True
                pair1 = False
                pair2 = False
                skip = False

                counter1 = 0

                for x in numInpt[:6]:
                    if numInpt[counter1 + 1] == x + 1:
                        if numInpt[counter1 + 2] == x + 2:
                            run = True
                    else:
                        counter1 += 1

                for x in numInpt:
                    if x == ord('i') - 96 or x == ord('o') - 96 or x == ord('l') - 96:
                        trick = True
                    else:
                        trick = False

                counter2 = 0

                for x in numInpt[:7]:
                    if x == numInpt[counter2 + 1]:
                        if skip == True:
                            skip = False
                        elif pair1 == False:
                            pair1 = True
                            skip = True
                        else:
                            pair2 = True
                    else:
                        skip = False

                    counter2 += 1

                if run == True and trick == False and pair2 == True:
                    oupt = ''
                    for x in numInpt:
                        oupt += chr(x + 96)

                    return oupt

                    break

                else:
                    for x in range(7, 0, -1):
                        if numInpt[x] != 26:
                            numInpt[x] += 1
                            break
                        else:
                            numInpt[x] = 1

        #Part 1
        solution1 = solution(part1_input)

        #Part 2
        sol2_interate = []
        for char in solution1:
            number = ord(char) - 96
            sol2_interate.append(number)
        for x in range(7, 0, -1):
            if sol2_interate[x] != 26:
                sol2_interate[x] += 1
                break
            else:
                sol2_interate[x] = 1
        sol2_input = ''
        for x in sol2_interate:
            sol2_input += chr(x + 96)

        solution2 = solution(sol2_input)

        return solution1, solution2

#Day 12
    def day12_2015(part1_input):
        import ast

        txt = part1_input.decode("utf-8") #the file reads in as a bytes (b') type - need to convert it to string type

        #Part 1
        lst = list(txt)
        counter = 0
        total = 0
        string = ''

        for x in lst:
            if ord(x) >= 48 and ord(x) <= 57:
                string = string + x
                if ord(lst[counter + 1]) >= 48 and ord(lst[counter + 1]) <= 57:
                    pass
                else:
                    num = int(string)
                    total = total + num
                    string = ''

            elif x == '-' and ord(lst[counter + 1]) >= 48 and ord(lst[counter + 1]) <= 57:
                string = string + x
            counter += 1

        solution1 = total

        #Part 2
        def loop(x, count, typ):
            valueX = 0
            level = count
            for a in x:
                if type(a) is dict:
                    output = loop(a.values(), level + 1, 'd')
                    valueX += output

                elif type(a) is list or type(a) is tuple:
                    output = loop(a, level + 1, 'l')
                    valueX += output

                else:
                    if a == 'red' and typ == 'd':
                        valueX = 0
                        break
                    elif a == 'red' and typ == 'l':
                        pass
                    elif type(a) is int:
                        valueX += a

            return valueX

        solution2 = loop(ast.literal_eval(txt), 0, 'l') #ast.literal_eval reads the string representation of a list as an actual list

        return solution1, solution2

#Day 13
    def day13_2015(part1_input):
        import itertools

        split_input = part1_input.split()
        input_list = []
        counter = 0
        while counter < len(split_input):
            if split_input[counter][-1] == '.':
                input_list += [' '.join(split_input[:(counter + 1)])]
                split_input = split_input[(counter + 1):]
                counter = 0
            else:
                counter += 1

        input_list_of_lists = []
        for line in input_list:
            input_list_of_lists += [line.split(' ')]

        guests = []
        for line in input_list_of_lists:
            # print(line)
            name = line[0]
            if name not in guests:
                guests += [name]

        register = {}
        for guest in guests:
            otherGuests = guests.copy()
            otherGuests.remove(guest)
            register[guest] = {}
            for otherGuest in otherGuests:
                for instruction in input_list_of_lists:
                    if instruction[0] == guest and instruction[-1] == (otherGuest + '.'):
                        if instruction[2] == 'lose':
                            register[guest][otherGuest] = int('-' + instruction[3])
                        elif instruction[2] == 'gain':
                            register[guest][otherGuest] = int(instruction[3])
                        else:
                            print('Recognition error in ' + str(step))

        options = []
        fullOptions = []
        options = list(itertools.permutations(guests, len(guests)))
        for option in options:
            fullOptions += [option + (option[0],)]
        best_arrangement = []
        topScore = 0
        for option in fullOptions:
            counter = 0
            score = 0
            while counter <= len(guests) - 1:
                score += register[option[counter]][option[counter + 1]]
                score += register[option[counter + 1]][option[counter]]
                counter += 1
            if score >= topScore:
                topScore = score
                best_arrangement = option

        solution1 = topScore

        #Part 2
        for dic in register:
            register[dic]['Jono'] = 0
        register['Jono'] = {}
        for guest in guests:
            register['Jono'][guest] = 0
        guests.append('Jono')

        options = []
        fullOptions = []
        options = list(itertools.permutations(guests, len(guests)))
        for option in options:
            fullOptions += [option + (option[0],)]
        best_arrangement = []
        topScore = 0
        for option in fullOptions:
            counter = 0
            score = 0
            while counter <= len(guests) - 1:
                score += register[option[counter]][option[counter + 1]]
                score += register[option[counter + 1]][option[counter]]
                counter += 1
            if score >= topScore:
                topScore = score
                best_arrangement = option

        solution2 = topScore

        return solution1, solution2

#Day 14
    def day14_2015(part1_input):
        import pandas as pd

        split_input = part1_input.split()
        input_list = []
        counter = 0
        while counter < len(split_input):
            if split_input[counter][-1] == '.':
                input_list += [' '.join(split_input[:(counter + 1)])]
                split_input = split_input[(counter + 1):]
                counter = 0
            else:
                counter += 1

        input_list_of_lists = []
        for line in input_list:
            input_list_of_lists += [line.split(' ')]

        data = pd.DataFrame()  # {'Name':[], 'Speed':[], 'Endurance':[], 'Rest':[]})

        for line in input_list_of_lists:
            data = data.append(
                {'Name': line[0], 'Speed': int(line[3]), 'Endurance': int(line[6]), 'Rest': int(line[-2])},
                ignore_index=True)

        timeStep = 2503

        for id, row in data.iterrows():

            cycles = timeStep // (data['Endurance'][id] + data['Rest'][id])
            finalDash = timeStep % (data['Endurance'][id] + data['Rest'][id])
            if finalDash <= data['Endurance'][id]:
                distance = (cycles * data['Endurance'][id] + finalDash) * data['Speed'][id]
            else:
                distance = (cycles + 1) * data['Endurance'][id] * data['Speed'][id]

            data.loc[id, "Distance"] = distance

        solution1 = str(int(max(data["Distance"])))

        #Part 2
        data2 = pd.DataFrame()  # {'Name':[], 'Speed':[], 'Endurance':[], 'Rest':[]})

        for line in input_list_of_lists:
            data2 = data.append(
                {'Name': line[0], 'Speed': int(line[3]), 'Endurance': int(line[6]), 'Rest': int(line[-2])},
                ignore_index=True)

        data['Points'] = pd.Series([0 for x in range(len(data.index))], index=data.index)

        for timeStep in range(1, 2504):

            for id, row in data.iterrows():
                cycles = timeStep // (data['Endurance'][id] + data['Rest'][id])
                finalDash = timeStep % (data['Endurance'][id] + data['Rest'][id])
                if finalDash <= data['Endurance'][id]:
                    distance = (cycles * data['Endurance'][id] + finalDash) * data['Speed'][id]
                else:
                    distance = (cycles + 1) * data['Endurance'][id] * data['Speed'][id]

                data.loc[id, "Distance"] = distance

            for id, row in data.iterrows():
                if data['Distance'][id] == max(data["Distance"]):
                    data.loc[id, "Points"] += 1

            if timeStep % 500 == 0:
                print('Completed ' + str(timeStep) + ' seconds.')

        solution2 = max(data["Points"])

        return solution1, solution2

#Day 15
    def day15_2015(part1_input):
        import pandas as pd
        import re

        split_input = part1_input.split()
        input_list = []
        counter = 1
        while counter < len(split_input):
            if split_input[counter][-1] == ':':
                input_list += [' '.join(split_input[:(counter)])]
                split_input = split_input[(counter):]
                counter = 0
            else:
                counter += 1

        input_list_of_lists = []
        for line in input_list:
            input_list_of_lists += [line.split(' ')]

        data = pd.DataFrame()
        for line in inpt:
            data = data.append({'Name': line[0], 'Capacity': int(re.sub("[^\d\-]", "", line[2])),
                                'Durability': int(re.sub("[^\d\-]", "", line[4])),
                                'Flavor': int(re.sub("[^\d\-]", "", line[6])),
                                'Texture': int(re.sub("[^\d\-]", "", line[8])),
                                'Calories': int(re.sub("[^\d\-]", "", line[10]))}, ignore_index=True)

        ingredients = data['Name'].tolist()
        print(ingredients)

        recipe = {}
        for row in data['Name']:
            recipe[row] = 0
        print(recipe)

        data.set_index('Name', inplace=True, drop=True)
        print(data)

        def ingred(index, recipe, topScore):
            spaceLeft = totalTeaspoons
            for x in range(0, index):
                spaceLeft -= recipe.get(ingredients[x])
            if index <= len(recipe) - 2:
                for n in range(0, spaceLeft + 1):
                    recipe[ingredients[index]] = n
                    index += 1
                    index, recipe, topScore = ingred(index, recipe, topScore)
            else:
                recipe[ingredients[index]] = spaceLeft
                capacity = 0
                for x in range(len(ingredients)):
                    capacity += data.at[ingredients[x], 'Capacity'] * recipe[ingredients[x]]
                durability = 0
                for x in range(len(ingredients)):
                    durability += data.at[ingredients[x], 'Durability'] * recipe[ingredients[x]]
                flavor = 0
                for x in range(len(ingredients)):
                    flavor += data.at[ingredients[x], 'Flavor'] * recipe[ingredients[x]]
                texture = 0
                for x in range(len(ingredients)):
                    texture += data.at[ingredients[x], 'Texture'] * recipe[ingredients[x]]

                if capacity <= -1 or durability <= -1 or flavor <= -1 or texture <= -1:
                    score = 0
                else:
                    score = capacity * durability * flavor * texture

                if score >= topScore + 1:
                    topScore = score

            index -= 1
            return index, recipe, topScore
        totalTeaspoons = 100
        solution1 = ingred(0, recipe, 0)[2]

        #Part 2
        def calor(index, recipe, topScore):
            spaceLeft = totalTeaspoons
            for x in range(0, index):
                spaceLeft -= recipe.get(ingredients[x])
            if index <= len(recipe) - 2:
                for n in range(0, spaceLeft + 1):
                    recipe[ingredients[index]] = n
                    index += 1
                    index, recipe, topScore = calor(index, recipe, topScore)

            else:
                recipe[ingredients[index]] = spaceLeft

                capacity = 0
                for x in range(len(ingredients)):
                    capacity += data.at[ingredients[x], 'Capacity'] * recipe[ingredients[x]]
                durability = 0
                for x in range(len(ingredients)):
                    durability += data.at[ingredients[x], 'Durability'] * recipe[ingredients[x]]
                flavor = 0
                for x in range(len(ingredients)):
                    flavor += data.at[ingredients[x], 'Flavor'] * recipe[ingredients[x]]
                texture = 0
                for x in range(len(ingredients)):
                    texture += data.at[ingredients[x], 'Texture'] * recipe[ingredients[x]]
                calories = 0
                for x in range(len(ingredients)):
                    calories += data.at[ingredients[x], 'Calories'] * recipe[ingredients[x]]

                if capacity <= -1 or durability <= -1 or flavor <= -1 or texture <= -1:
                    score = 0
                elif calories != 500:
                    score = 0
                else:
                    score = capacity * durability * flavor * texture
                if score >= topScore + 1:
                    topScore = score

            index -= 1
            return index, recipe, topScore

            totalTeaspoons = 100
            solution2 = calor(0, recipe, 0)[2]

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
        if day == "9": solution1, solution2 = day9_2015(part1_input)
        if day == "10": solution1, solution2 = day10_2015(part1_input)
        if day == "11": solution1, solution2 = day11_2015(part1_input)
        if day == "12": solution1, solution2 = day12_2015(part1_input)
        if day == "13": solution1, solution2 = day13_2015(part1_input)
        if day == "14": solution1, solution2 = day14_2015(part1_input)
        if day == "15": solution1, solution2 = day15_2015(part1_input)

    return solution1, solution2