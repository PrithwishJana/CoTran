import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def fact(n):
        ans = 1
        for i in range(1, n + 1):
            ans = ans * i
        return (ans)
    @staticmethod
    def numberOfPossiblePallindrome(str, n):
        mp = {}
        for i in range(0, n):
            mp[str[i]] = 1 if mp[str[i]] is None else mp[str[i]] + 1
        k = 0
        num = 0
        den = 1
        fi = 0
        for it in mp.entrySet():
            if math.fmod(it.getValue(), 2) == 0:
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                fi = it.getValue() / 2
            else:
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                fi = (it.getValue() - 1) / 2
                k += 1
            num = num + fi
            den = den * GFG.fact(fi)
        if num != 0:
            num = GFG.fact(num)
        ans = math.trunc(num / float(den))
        if k != 0:
            ans = ans * k
        return (ans)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "ababab"
        n = len(str)
        print(GFG.numberOfPossiblePallindrome(str, n))
