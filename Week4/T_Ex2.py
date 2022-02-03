''''
Find duplicates in a list without using sets
'''

some_list = ['a', 'b', 'c', 'b', 'd', 'a', 'm', 'n', 'n']
other_list = []

for i in some_list:
    if i not in other_list:
        other_list.append(i)
    else:
        print(f"{i} is a duplicate.")
