import math

class codeNinetySeven:
    @staticmethod
    def main(args):
        input = Scanner(System.in)
        m = input.nextInt()
        n = input.nextInt()
        arrayOne = [['\0' for _ in range(n)] for _ in range(m)]
        for i in range(0, m):
            data = ""
            if input.hasNext():
                data = input.next()
            else:
                break
            for j in range(0, n):
                arrayOne [i][j] = data[j]
        sumr = 0
        sumc = 0
        count1 = 0
        count2 = 0
        for i in range(0, m):
            for j in range(0, n):
                if arrayOne [i][j] == chr(66):
                    sumr += i + 1
                    count1 += 1
        for i in range(0, m):
            for j in range(0, n):
                if arrayOne [i][j] == chr(66):
                    sumc += j + 1
                    count2 += 1
        print(math.trunc(sumr / float(count1)) + " " + math.trunc(sumc / float(count2)))
