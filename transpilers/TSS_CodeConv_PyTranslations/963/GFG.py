import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countNumber(n):
        result = 0
        for i in range(1, 10):
            s = java.util.Stack()
            if i <= n:
                s.push(i)
                result += 1
            while not s.empty():
                tp = s.peek()
                s.pop()
                for j in range(math.fmod(tp, 10), 10):
                    x = tp * 10 + j
                    if x <= n:
                        s.push(x)
                        result += 1
        return result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 15
        print(GFG.countNumber(n))
