import re

def part1():
    with open("./input.txt", "r") as file:
        data = file.read()
    
    regex = r'mul\(([0-9]+),([0-9]+)\)';
    sum = 0;

    matches = re.findall(regex, data)

    for numb in matches:
        sum += int(numb[0]) * int(numb[1])

    return sum;




if __name__ == "__main__":
    print(part1())