class JavaApplication38:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        num1 = sc.nextInt()
        num2 = sc.nextInt()
        counter = 0
        while num1 != 0 and num2 != 0:
            if num1 == 1 and num2 == 1:
                break
            if num1 <= num2:
                num1 += 1
                num2 -= 2
            else:
                num1 -= 2
                num2 += 1
            counter += 1
        print(counter)
