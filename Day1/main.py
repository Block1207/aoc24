def part1():
    left = [];
    right = [];
    dist = 0;

    with open('./input.txt', 'r') as file:
        lines = file.read().splitlines()    

    for line in lines:
        numbers = line.split();
        left.append(numbers[0])
        right.append(numbers[1])

    left.sort();
    right.sort();

    for i in range(0, len(left)):
        dist += abs(int(left[i]) - int(right[i]))
    
    print(dist)

def part2():
    left = [];
    right = [];
    sim = 0;

    with open('./input.txt', 'r') as file:
        lines = file.read().splitlines()    

    for line in lines:
        numbers = line.split();
        left.append(numbers[0])
        right.append(numbers[1])
    
    for number in left:
        count = 0
        for number2 in right:
            if number == number2:
                count += 1
        sim += int(number) * count

    print(sim)
        

            

    

if __name__ == "__main__":
    #part1();
    part2();