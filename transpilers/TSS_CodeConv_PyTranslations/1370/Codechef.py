class Codechef:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.lang.Exception
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        try:
            sc = Scanner(System.in)
            n = sc.nextInt()
            a = [0 for _ in range(n)]
            b = [0 for _ in range(n)]
            sum = 0
            for i in range(0, n):
                a [i] = sc.nextInt()
                sum += a [i]
            for i in range(0, n):
                b [i] = sc.nextInt()
            Arrays.sort(b)
            ans = b [n - 1] + b [n - 2]
            if sum <= ans:
                print("YES")
            else:
                print("NO")
        except Exception as e:
            pass
