def rabbit_breed():
    female_r = int(input("Please enter the number of female rabbits:"))
    male_r = int(input("Please enter the number of male rabbits:"))
    if female_r > 0 and male_r > 0:
        answer = input("Do you want to breed?").lower()
        if answer == "no":
            print("Keep male and female rabbits apart!")
        else:
            print("Breed ok.")
rabbit_breed()