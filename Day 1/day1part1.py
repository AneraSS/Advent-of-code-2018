# https://adventofcode.com/2018/day/1

with open ('input.txt') as file:
    resulting_frequency = 0
    for line in file:
        resulting_frequency += int(line)

print (resulting_frequency)
