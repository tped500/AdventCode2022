# New lines represent new inventory
# Each line represents calories of an item
import numpy as np

with open('input.txt') as file:
    lines = [line.replace(str('\n'), "") for line in file]

most_calories = []
current_elf = 0
for i in range(len(lines)):
    if lines[i] != '':
        if i == len(lines)-1:
            current_elf += int(lines[i])
            most_calories.append(current_elf)
            # if current_elf > min(top_three):
            #     top_three = top_three.replace(min(top_three), current_elf)
        else:
            current_elf += int(lines[i])
            # print(f"Current Elf... {current_elf}")
    else:
        # print('\n')
        most_calories.append(current_elf)
        # if current_elf > most_calories:
        #     most_calories = current_elf
        current_elf = 0

top_three = np.sort(most_calories)[::-1]
final_three = 0
for top in top_three[:3]:
    final_three += top

print(final_three)