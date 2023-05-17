import math

class JavaApplication70:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        num = sc.nextInt()
        counter = 0
        fine = 0
        arr = []
        for i in range(0, num):
            s = sc.next()
            arr.append(s)
        for i in range(0, num):
            for k in range(0, num):
                if arr[k][i] == 'C':
                    counter += 1
            fine += math.trunc((counter * (counter - 1)) / float(2))
            counter = 0
        for i in range(0, num):
            for k in range(0, num):
                if arr[i][k] == 'C':
                    counter += 1
            fine += math.trunc((counter * (counter - 1)) / float(2))
            counter = 0
        print(fine)
