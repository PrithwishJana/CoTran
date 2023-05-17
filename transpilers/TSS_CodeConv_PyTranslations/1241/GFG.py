import math

class GFG:
    @staticmethod
    def check_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if math.fmod(n, 2) == 0 or math.fmod(n, 3) == 0:
            return False
        i = 5
        while i * i <= n:
            if math.fmod(n, i) == 0 or math.fmod(n, (i + 2)) == 0:
                return False
            i = i + 6
        return True
    @staticmethod
    def countPrimeFrequent(s):
        count = 0
        mp = {}
        i = 0
        while i < len(s):
            if s[i] in mp.keys():
                mp[s[i]] = mp[s[i]] + 1
            else:
                mp[s[i]] = 1
            i += 1
        for entry in mp.entrySet():
            if GFG.check_prime(entry.getValue()):
                count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "geeksforgeeks"
        print(GFG.countPrimeFrequent(s))
