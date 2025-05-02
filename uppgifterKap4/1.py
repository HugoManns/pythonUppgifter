looping_list = [0, 'a', 'b', [1, 2, 3], ('Python', 'R', 'C', 'Java'), 55]

for item in looping_list:
    print(item)

print( '---------')
for item in enumerate(looping_list):
    print(item)