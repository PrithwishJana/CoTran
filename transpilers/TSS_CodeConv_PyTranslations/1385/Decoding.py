import math

class Decoding:
    @staticmethod
    def main(args):
        reader = java.util.Scanner(System.in)
        n = reader.nextInt()
        s = ['\0' for _ in range(n)]
        newS = ['\0' for _ in range(n)]
        input = reader.next()
        s = input.toCharArray()
        mid = math.trunc((n - 1) / float(2))
        counter = 0
        for i in range(0, n):
            temp = i + 1
            if math.fmod(n, 2) == 0:
                newS [mid - counter] = s [i]
            else:
                newS [mid + counter] = s [i]
            if counter >= 0:
                counter = counter - temp
            else:
                counter = counter + temp
        print(str(newS))
