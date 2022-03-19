from abc import ABC, abstractmethod  # abstract base class


class TestModel(ABC):
    @abstractmethod
    def setup(self):
        raise NotImplemented

    @abstractmethod
    def execute(self):
        raise NotImplemented

    @abstractmethod
    def tear_down(self):
        raise NotImplemented


class Test1(TestModel):
    def setup(self):
        print("Implement")

    def execute(self):
        print("Execute test 1.")

    def tear_down(self):
        print("Close the browser")


class Test2(TestModel):
    def setup(self):
        print("Implement test 2")

    def execute(self):
        print("Execute test 2.")

    def tear_down(self):
        print("Close the browser 2")


if __name__ == '__main__':
    test1 = Test1()
    test2 = Test2()

    for test in test1, test2: #polimorfism
        test.setup()
        test.execute()
        test.tear_down()
