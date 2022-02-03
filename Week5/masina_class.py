class CarDealer:
    def __init__(self, culoare, cap_motor, nr_usi, comb):
        self._culoare = culoare  # self._culoare = atribute de instanta
        self._cap_motor = cap_motor
        self._nr_usi = nr_usi
        self._comb = comb

    def build_offer(self, budget):
        if budget > 30000:
            print(f"You can buy a Mercedes C Class with color {self._culoare}.")
        elif 30000 > budget > 10000:
            print(f"You can buy a Renault Megane with color {self._culoare}.")
        else:
            print("Your preferences are ignored, but you can still buy a Dacia Logan.")


dealer = CarDealer("red", 1.5, 5, "gas")

dealer.build_offer(20000)
dealer.build_offer(35000)
dealer.build_offer(9000)
