class Calculator:
    num = 100

    def __init__(self, a, b):
        print("Initiated calculation of below two numbers")
        self.op1 = a
        self.op2 = b
        print(str(self.op1) + " & " + str(self.op2))

    def sum(self):
        return self.op1 + self.op2

    def minus(self):
        return self.op1 - self.op2

    def product(self):
        return self.op1 * self.op2

    def divide(self):
        if self.op2 == 0:
            return "infinity"
        else:
            return self.op1 // self.op2

    def percentage(self):
        if self.op1 <= self.op2:
            return (self.op1 / self.op2) * Calculator.num


# operator = ['+', '-', '*', '/', 'per']
# inp1, opr, inp2 = input("Enter two number separating spaces: ").split(" ")
# c = Calculator(int(inp1), int(inp2))
#
# if opr == operator[0]:
#     result = c.sum()
#
# elif opr == operator[1]:
#     result = c.minus()
#
# elif opr == operator[2]:
#     result = c.product()
#
# elif opr == operator[3]:
#     result = c.divide()
#
# elif opr == operator[4]:
#     result = c.percentage()
#
# else:
#     print("Undefined operator!!")
#
# print(str(inp1) + opr + str(inp2) + "=" + str(result))