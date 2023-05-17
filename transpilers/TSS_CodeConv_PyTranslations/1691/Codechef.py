class Codechef:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.lang.Exception
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = Scanner(System.in)
        n = sc.nextLong()
        k = sc.nextLong()
        arr = [0 for _ in range(int(n))]
        i = 0
        while i < int(n):
            arr [int(i)] = sc.nextLong()
            i += 1
        if k == 1:
            print(n)
            System.exit(0)
        ans = [0 for _ in range(int(n))]
        Arrays.sort(arr)
        i = 0
        while i < int(n):
            if ans [int(i)] == 0:
                ktimes = k * arr [int(i)]
                index = Arrays.binarySearch(arr, ktimes)
                if index >= 0:
                    ans [int(index)] = - 1
            i += 1
        ans1 = 0
        for i in range(0, n):
            if ans [int(i)] == 0:
                ans1 += 1
        print(ans1)
