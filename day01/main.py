from locker_v2 import BreakLocker

locker = BreakLocker(position=50)

with open("C:/projects/aoc2025/day01/input.txt", "r") as file:
    for row in file:
        row = row.strip()
        direction = row[0]
        value = int(row[1:].strip())

        if direction == "L":
            locker.calculate_left(value)
        else:
            locker.calculate_right(value)

    print(locker.count)
