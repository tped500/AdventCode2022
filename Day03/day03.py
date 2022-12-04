"""
The Elves have made a list of all of the items currently in each rucksack (your puzzle input),
but they need your help finding the errors. Every item type is identified by a single lowercase or
uppercase letter (that is, a and A refer to different types of items).


The list of items for each rucksack is given as characters all on a single line.
A given rucksack always has the same number of items in each of its two compartments,
so the first half of the characters represent items in the first compartment,
while the second half of the characters represent items in the second compartment.


To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.

In the above example, the priority of the item type that appears in both compartments of each rucksack is
16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack.
What is the sum of the priorities of those item types?
"""
### Part 1

with open('input.txt') as file:
    lines = [line.replace(str('\n'), "") for line in file]

sum_items = 0
for i in range(len(lines)):
    first_compartment, second_compartment = lines[i][:len(lines[i]) // 2], lines[i][len(lines[i]) // 2:]
    common_element = set(list(first_compartment)).intersection(second_compartment)

    if list(common_element)[0].islower():
        sum_items += ord(list(common_element)[0]) - (ord('a') - 1)
    else:
        sum_items += ord(list(common_element)[0].lower()) - (ord('a')-1) + 26


# print(sum_items)

### Part 2
with open('input.txt') as file:
    lines = [line.replace(str('\n'), "") for line in file]

sum_items = 0

for i in range(0, len(lines), 3):
    list_of_elves = lines[i:i+3]
    first_elf, second_elf, third_elf = list_of_elves[0], list_of_elves[1], list_of_elves[2]
    badge_sticker = set(list(first_elf)).intersection((set(list(second_elf)).intersection(third_elf)))

    if list(badge_sticker)[0].islower():
        sum_items += ord(list(badge_sticker)[0]) - (ord('a') - 1)
    else:
        sum_items += ord(list(badge_sticker)[0].lower()) - (ord('a')-1) + 26

print(sum_items)