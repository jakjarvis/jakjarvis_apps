import advent.solutions15 as solution15
import advent.solutions16 as solution16
import advent.solutions21 as solution21

def solution(year, day, part1_input, part2_input):

    if year == "2015":
        if day == "1": solution1, solution2 = solution15.day1_2015(part1_input)
        elif day == "2": solution1, solution2 = solution15.day2_2015(part1_input)
        elif day == "3": solution1, solution2 = solution15.day3_2015(part1_input)
        elif day == "4": solution1, solution2 = solution15.day4_2015(part1_input)
        elif day == "5": solution1, solution2 = solution15.day5_2015(part1_input)
        elif day == "6": solution1, solution2 = solution15.day6_2015(part1_input)
        elif day == "7": solution1, solution2 = solution15.day7_2015(part1_input)
        elif day == "8": solution1, solution2 = solution15.day8_2015(part1_input)
        elif day == "9": solution1, solution2 = solution15.day9_2015(part1_input)
        elif day == "10": solution1, solution2 = solution15.day10_2015(part1_input)
        elif day == "11": solution1, solution2 = solution15.day11_2015(part1_input)
        elif day == "12": solution1, solution2 = solution15.day12_2015(part1_input)
        elif day == "13": solution1, solution2 = solution15.day13_2015(part1_input)
        elif day == "14": solution1, solution2 = solution15.day14_2015(part1_input)
        elif day == "15": solution1, solution2 = solution15.day15_2015(part1_input)
        elif day == "16": solution1, solution2 = solution15.day16_2015(part1_input)
        elif day == "17": solution1, solution2 = solution15.day17_2015(part1_input)
        elif day == "18": solution1, solution2 = solution15.day18_2015(part1_input)
        elif day == "19": solution1, solution2 = solution15.day19_2015(part1_input, part2_input)
        elif day == "20": solution1, solution2 = solution15.day20_2015(part1_input)
        elif day == "21": solution1, solution2 = solution15.day21_2015(part1_input)
        elif day == "22": solution1, solution2 = solution15.day22_2015(part1_input)
        elif day == "23": solution1, solution2 = solution15.day23_2015(part1_input)
        elif day == "24": solution1, solution2 = solution15.day24_2015(part1_input)
        elif day == "25": solution1, solution2 = solution15.day25_2015(part1_input, part2_input)

    elif year == "2016":
        if day == "1": solution1, solution2 = solution16.day1_2016(part1_input)
        elif day == "2": solution1, solution2 = solution16.day2_2016(part1_input)
        elif day == "3": solution1, solution2 = solution16.day3_2016(part1_input)
        elif day == "4": solution1, solution2 = solution16.day4_2016(part1_input)
        elif day == "5": solution1, solution2 = solution16.day5_2016(part1_input)
        elif day == "6": solution1, solution2 = solution16.day6_2016(part1_input, part2_input)
        else: solution1, solution2 = solution16.error(part1_input)

    elif year == "2021":
        if day == "1": solution1, solution2 = solution21.day1_2021(part1_input)
        if day == "2": solution1, solution2 = solution21.day2_2021(part1_input)
        if day == "3": solution1, solution2 = solution21.day3_2021(part1_input)
        else: solution1, solution2 = solution21.error(part1_input)


    return solution1, solution2