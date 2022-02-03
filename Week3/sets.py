my_set = {4, 2, 8, 5, 10, 11, 10} # seturile sunt neordonate
my_set2 = {9, 5, 77, 22, 98, 11, 10}
print(my_set)

# print(my_set[0:]) #nu se poate

lst = (11, 12, 12, 14, 15, 13, 14)
print(set(lst)) #eliminam duplicatele din lista prin transformarea in set

print(my_set.difference(my_set2))
print(my_set.intersection(my_set2))