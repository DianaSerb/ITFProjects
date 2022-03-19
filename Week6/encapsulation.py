class Encapsulation:
    def set_public(self):
        print("I am visible to the entire project.")

    def _set_protected(self):  # _ inainte de metoda indica faptul ca e protected
        print("I am visible by child")

    def __set_private(self):
        print("I am not visible outside the class")

    def get(self):
        self.__set_private()


class Child(Encapsulation):
    def test(self):
        self.set_public()
        self._set_protected()


y = Child()
y.test()

x = Encapsulation()
x._set_protected()
# x.__set_private()
x.set_public()
x.get()
