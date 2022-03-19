from overload import overload


class TestCase:
    @overload
    def run(self, a):
        print("This is method " + a)

    @run.add
    def run(self, a, b):
        print("This is method " + a + b)

    @run.add
    def run(self, a, b, c):
        print("This is method nr 3")

testcase = TestCase()
testcase.run("a")
testcase.run("a", "b")
testcase.run("a", "b", "c")