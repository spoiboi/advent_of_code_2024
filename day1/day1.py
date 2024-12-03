text = open("day1Input", "r")
left_list = []
right_list = []

# Convert to lists
for line in text.readlines():
    left_list.append(int(line.split()[0]))
    right_list.append(int(line.split()[1]))

# sort
left_list.sort()
right_list.sort()

# sum of difs
sum = 0
"""
print(left_list[0])
print(right_list[0])
print(abs(left_list[0]-right_list[0]))
"""

for i in range(len(left_list)):
    sum += (abs(left_list[i]-right_list[i]))

print(sum)

