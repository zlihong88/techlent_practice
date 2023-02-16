class Calculator():
    def add(self, num1, num2):
       # return num1+num2
        return 2
    def devide(self, num1, num2):
        if num2 == 0:
            return 0
        return num1 / num2

if __name__=='__main__':
    calculator = Calculator()
    print(calculator.add(1,3))
    print(calculator.devide(10,0))
    print(calculator.devide(10,2))
