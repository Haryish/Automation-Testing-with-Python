from ClassAndObjectDemo import Calculator


class ChildCalc(Calculator):
    num2 = 1000

    def __init__(self):
        Calculator.__init__(self, 5, 4)

    def getSum(self):
        return self.num2 + self.num + self.sum()


obj = ChildCalc()
print("The sum: " + str(obj.getSum()))
