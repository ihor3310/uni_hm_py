class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error"


def main():
    print("Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    calc = Calculator(num1, num2)

    print("Choose an operation:")
    print("[1] + ")
    print("[2] - ")
    print("[3] * ")
    print("[4] ÷ ")

    operation = input("Choose the operation (1 | 2 | 3 | 4): ")

    if operation == '1':
        result = calc.add()
        print(f"The result of addition is: {result}")
    elif operation == '2':
        result = calc.subtract()
        print(f"The result of subtraction is: {result}")
    elif operation == '3':
        result = calc.multiply()
        print(f"The result of multiplication is: {result}")
    elif operation == '4':
        result = calc.divide()
        print(f"The result of division is: {result}")
    else:
        print("[1-4]")


if __name__ == "__main__":
    main()
