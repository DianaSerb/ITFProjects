my_tuple = (1, 2, 5, 8, 12)  # tupla
my_list = [13, 28, 36, 44]  # lista

print(type(my_list))
print(my_tuple[3:])  # slicing tuple

new_tuple = tuple(my_list)
print(my_list)
print(type(new_tuple))

print(1 in my_tuple)

print(new_tuple[:3])

x, y, z, *other = (7, 18, 29, 5, 1, 10, 34)
print(other)

last_tuple = 12, 13, 56, 35, 42 #tuplele se pot defini si fara paranteze rotunde
print(last_tuple)

last_tuple.append(7) #nu se poate