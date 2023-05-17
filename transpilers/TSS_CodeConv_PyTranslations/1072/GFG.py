import math

class GFG:
    @staticmethod
    def createSorted(a, n):
        b = list  ()
        for j in range(0, n):
            if not b:
                b.append(a [j])
            else:
                start = 0
                end = len(b) - 1
                pos = 0
                while start <= end:
                    mid = start + math.trunc((end - start) / float(2))
                    if b[mid] == a [j]:
                        b.insert((max(0, mid + 1)), a [j])
                        break
                    elif b[mid] > a [j]:
                        pos = end = mid - 1
                    else:
                        pos = start = mid + 1
                    if start > end:
                        pos = start
                        b.insert(max(0, pos), a [j])
                        break
        for i in range(0, n):
            print(str(b[i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [2, 5, 4, 9, 8]
        n = len(a)
        GFG.createSorted(a, n)
