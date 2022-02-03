x = 'expected result'
y = 'expected result'

if x == y and type(x) == type(y):
    print("Test passed")
else:
    print("Test failed")

if x == y:
    if type(x) is int:
        print("Test failed") #nested if
    elif type(x) is str:     #elif -> else if
        print("Test passed")
    else:
        print("Test failed")
else:
    print("Test failed")

