import copy

def part1():
    with open('./input.txt', 'r') as file:
        lines = file.read().splitlines();
    
    safe = 0

    for line in lines:
        line = line.split()

        if is_save(line):
            safe += 1
    
    return safe


def part2():
    with open('./input.txt', 'r') as file:
        lines = file.read().splitlines();
    
    safe = 0

    for line in lines:
        line = line.split()

        for i in range(len(line)):
            rest = line[:i] + line[i+1:]
            if is_save(rest):
                safe += 1
                break
    
    return safe

def is_save(line):
    asc = False

    if(int(line[0]) < int(line[1])):
        asc = True

    for i in range(1, len(line)):
        if asc and int(line[i]) < int(line[i-1]):
            return False
        elif not asc and int(line[i]) > int(line[i-1]):
            return False
        elif int(line[i]) == int(line[i-1]):
            return False
        if abs(int(line[i]) - int(line[i-1])) > 3 or abs(int(line[i]) - int(line[i-1])) < 1:
            return False

    return True

if __name__ == "__main__":
    print(part1())
    print(part2())