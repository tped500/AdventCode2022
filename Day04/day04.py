### part 1 and 2 together
with open('input.txt') as file:
    lines = [line.replace(str('\n'), "").split(',') for line in file]

repeated_pairs = 0
overlap_pairs = 0
for i in range(len(lines)):
    first_set, second_set = set(range(int(lines[i][0].split('-')[0]), int(lines[i][0].split('-')[1]) + 1)),\
                            set(range(int(lines[i][1].split('-')[0]), int(lines[i][1].split('-')[1]) + 1))

    # part 1
    if first_set.issuperset(second_set) or second_set.issuperset(first_set):
        repeated_pairs += 1

    # part 2
    if first_set.intersection(second_set):
        overlap_pairs += 1

print(f'Repeated pairs: {repeated_pairs}')
print(f'Overlapped pairs: {overlap_pairs}')