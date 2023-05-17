class Factorial:
    def factorial(self, n):
        return 1 if (n == 1 or n == 0) else n * self.factorial(n - 1)
    @staticmethod
    def main(args):
        obj = Factorial()
        num = 5
        print("Factorial of " + str(num) + " is " + str(obj.factorial(num)))
