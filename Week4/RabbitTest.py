male_rabbits = int(input("Enter the number of male rabbits:"))
female_rabbits = int(input("Enter the number of female rabbits:"))

if male_rabbits > 0 and female_rabbits > 0:
    response = input("Do you want to breed?").lower()  # transforma inputul in lowercase
    if response == "no":
        print("Keep male and female rabbits apart!")
    else:
        print("Breed ok.")


# TODO convert this to a function (T_Ex4)

