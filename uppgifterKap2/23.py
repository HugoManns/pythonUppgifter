list_a = [1, 2, 3, 4, 5]
list_b = [5, 6, 10, 21]

set_list_a = set(list_a)
print(set_list_a)
set_list_b = set(list_b)
print(set_list_b)

intersection = set_list_a.intersection(set_list_b)
print(intersection)

union = set_list_a.union(set_list_b)
print(union)

diff = set_list_a.difference(set_list_b)
print(diff)

