import math

class CF_1447B_NumbersBox:
    @staticmethod
    def main(args):
        scanner = java.util.Scanner(System.in)
        count = scanner.nextInt()
        for i in range(0, count):
            n = scanner.nextInt()
            m = scanner.nextInt()
            arr = [0 for _ in range(n * m)]
            nagiviteTimes = 0
            minNum = Integer.MAX_VALUE
            sumNum = 0
            j = 0
            while j < len(arr):
                arr [j] = scanner.nextInt()
                if arr [j] < 0:
                    arr [j] = 0 - arr [j]
                    nagiviteTimes += 1
                    sumNum += arr [j]
                    if minNum > arr [j]:
                        minNum = arr [j]
                else:
                    sumNum += arr [j]
                    if minNum > arr [j]:
                        minNum = arr [j]
                j += 1
            if math.fmod(nagiviteTimes, 2) == 0:
                print(sumNum)
            else:
                print(sumNum - minNum * 2)
