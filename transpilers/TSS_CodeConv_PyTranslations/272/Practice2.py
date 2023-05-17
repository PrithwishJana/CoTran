class Practice2:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        n = sc.nextInt()
        list = []
        for i in range(0, n):
            list.append(sc.nextInt())
        for i in range(0, n):
            map = {}
            map[i + 1] = 1
            flag = 0
            j = i
            while flag == 0:
                if  list[j] not in map.keys():
                    map[list[j]] = 1
                else:
                    flag = 1
                    print(str(list[j]) + " ", end = '')
                j = list[j]
                j -= 1
