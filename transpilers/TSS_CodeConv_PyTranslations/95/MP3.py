class MP3:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        n = in_.nextInt()
        diskSize = in_.nextInt() * 8
        sounds = [0 for _ in range(n)]
        for i in range(0, n):
            sounds [i] = in_.nextInt()
        sounds.sort()
        distinctVals = [0 for _ in range(n)]
        distinctAmt = [0 for _ in range(n)]
        k = - 1
        for i in range(0, n):
            if i == 0 or sounds [i] > sounds [i - 1]:
                k += 1
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: distinctVals [++ k] = sounds [i];
                distinctVals [ k] = sounds [i]
                distinctAmt [k] = 1
            else:
                distinctAmt [k] += 1
        k += 1
        answer = n
        currAmt = distinctAmt [0]
        i = 0
        j = 0
        while i < k:
            while j < i or (j < k - 1 and n * MP3.lg(j + 1 - i + 1) <= diskSize):
                j += 1
                currAmt += distinctAmt [j]
            answer = min(answer, n - currAmt)
            currAmt -= distinctAmt [i]
            i += 1
        print(answer)
    @staticmethod
    def lg(n):
        res = 0
        while n > (1 << res):
            res += 1
        return res
