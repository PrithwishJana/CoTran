class ques:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = Scanner(System.in)
        t = sc.nextInt()
        for i in range(0, t):
            n = sc.nextInt()
            arr = [0 for _ in range(n)]
            arr2 = [0 for _ in range(n)]
            try:
                for j in range(0, n):
                    arr [j] = sc.nextInt()
                    arr2 [j] = j + 1
                j = 0
                while j < n - 1:
                    if arr2 [j] == arr [j]:
                        temp = arr2 [j]
                        arr2 [j] = arr2 [j + 1]
                        arr2 [j + 1] = temp
                    j += 1
                if arr2 [n - 1] == arr [n - 1]:
                    temp = arr2 [n - 1]
                    arr2 [n - 1] = arr2 [n - 2]
                    arr2 [n - 2] = temp
                for j in range(0, n):
                    print(str(arr2 [j]) + " ", end = '')
                print()
            except Exception as e:
                print(- 1)
