# förklara vad koden nedan gör!

my_list = []

for i in range(10):
    if i % 2 == 0:
        my_list.append(i)

print(my_list)

# Koden appendar jämna tal upp till 10 till listan my_list

new_list = []
list_example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list_example:
    if 4 <= num <= 8:
        new_list.append(num * 10)

print(new_list)

new_list = [num * 10 for num in list_example if 4 <= num <= 8]
print(new_list)