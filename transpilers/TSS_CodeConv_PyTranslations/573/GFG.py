class GFG:
    @staticmethod
    def compositeProduct(arr, n):
        max_val = Arrays.stream(arr).max().getAsInt()
        prime = [False for _ in range(max_val + 1)]
        Arrays.fill(prime, True)
        prime [0] = True
        prime [1] = True
        p = 2
        while p * p <= max_val:
            if prime [p] == True:
                for i in range(p * 2, max_val + 1, p):
                    prime [i] = False
            p += 1
        product = 1
        for i in range(0, n):
            if not prime [arr [i]]:
                product *= arr [i]
        return product
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 3, 4, 5, 6, 7]
        n = len(arr)
        print(GFG.compositeProduct(arr, n))
