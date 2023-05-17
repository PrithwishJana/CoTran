class Solution:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = Scanner(System.in)
        n = sc.nextInt()
        str = sc.next()
        S = 0
        i = 0
        while i < n - 1:
            if str[i] == 'S' and str[i + 1] == 'F':
                S += 1
            elif str[i] == 'F' and str[i + 1] == 'S':
                S -= 1
            i += 1
        if S > 0:
            print("YES")
        else:
            print("NO")
