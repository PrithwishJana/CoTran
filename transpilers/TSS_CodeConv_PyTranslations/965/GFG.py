class GFG:
    MAX = 1000000
    sieve_Prime = [0 for _ in range(MAX + 4)]
    sieve_count = [0 for _ in range(MAX + 4)]
    @staticmethod
    def form_sieve():
        GFG.sieve_Prime [1] = 1
        i = 2
        while i <= GFG.MAX:
            if GFG.sieve_Prime [i] == 0:
                j = i * 2
                while j <= GFG.MAX:
                    if GFG.sieve_Prime [j] == 0:
                        GFG.sieve_Prime [j] = 1
                        GFG.sieve_count [i] += 1
                    j += i
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.form_sieve()
        n = 2
        print("Count = " + str(GFG.sieve_count [n] + 1))
        n = 3
        print("Count = " + str(GFG.sieve_count [n] + 1))
