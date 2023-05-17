class geeks:
    @staticmethod
    def minOperations(a, n, K):
        map = {}
        for i in range(0, n):
            try:
                if map[a [i]]:
                    return 1
            except Exception as e:
                pass
            try:
                map[a [i]] = True
            except Exception as e:
                pass
        b = [0 for _ in range(n)]
        for i in range(0, n):
            b [i] = a [i] & K
        map.clear()
        for i in range(0, n):
            if a [i] != b [i]:
                try:
                    map[b [i]] = True
                except Exception as e:
                    pass
        for i in range(0, n):
            try:
                if map[a [i]]:
                    return 1
            except Exception as e:
                pass
        map.clear()
        for i in range(0, n):
            try:
                if map[b [i]]:
                    return 2
            except Exception as e:
                pass
            try:
                map[b [i]] = True
            except Exception as e:
                pass
        return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        K = 3
        a = [1, 2, 3, 7]
        n = len(a)
        print(geeks.minOperations(a, n, K))
