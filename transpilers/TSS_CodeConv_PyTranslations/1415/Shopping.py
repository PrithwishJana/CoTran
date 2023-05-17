class Shopping:
    def input(self, numberOne, numberTwo, numberThree):
        one = numberOne + numberTwo + numberThree
        two = 2 * (numberOne + numberTwo)
        three = 2 * (numberOne + numberThree)
        four = 2 * (numberTwo + numberThree)
        print(min(min(one, two), min(three, four)))
    @staticmethod
    def main(a):
        input = java.util.Scanner(System.in)
        instance = Shopping()
        numOne = input.nextInt()
        numTwo = input.nextInt()
        numThree = input.nextInt()
        instance.input(numOne, numTwo, numThree)
