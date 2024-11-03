class Factorial:
    cache = {}

    def __init__(self, n):
        self.n = n

    def calcul(self):
        if self.n in Factorial.cache:
            return Factorial.cache[self.n]
        if self.n == 0 or self.n == 1:
            Factorial.cache[self.n] = 1
            return 1
        result = self.n * Factorial(self.n - 1).calcul()
        Factorial.cache[self.n] = result
        return result

def main():
    n = int(input("Enter a number: "))
    factorial = Factorial(n)
    print(factorial.calcul())

if __name__ == "__main__":
    main()
