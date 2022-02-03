my_list = [22, 1, 3, 4]
suma = sum(my_list)
print(suma)

suma2 = 0
for i in my_list:
    suma2 = suma2 + i
else:
    print("Sum already calculated!")
print(suma2)

suma3 = 0
for i in range(0, len(my_list)):
    suma3 += my_list[i]
print(suma3)

# WHILE
x = 0
suma4 = 0
while x < len(my_list):
    suma4 += my_list[x]
    x += 1
print(suma4)

#TODO  Introducem un interval de numere (1,10) de la consola si sa generam random o valoare din acel interval, il rugam pe user sa
