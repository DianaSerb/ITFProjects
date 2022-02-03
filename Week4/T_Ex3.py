# get the highest even number from a specified list

def highest_even(lst):
    highest = 0
    for i in range(0, len(lst)):
        if lst[i] > highest and lst[i] % 2 == 0:
            highest = lst[i]
    print(highest)


print(highest_even([20,22,33,21,15,40]))
