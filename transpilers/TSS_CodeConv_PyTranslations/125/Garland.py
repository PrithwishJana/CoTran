class Garland:
    @staticmethod
    def main(args):
        s = Scanner(System.in)
        s1 = s.next()
        s2 = s.next()
        if Garland.isValid(s1, s2) == False:
            print(- 1)
        else:
            m1 = {}
            m2 = {}
            for c in s1.toCharArray():
                if c in m1.keys():
                    m1[c] = m1[c] + 1
                else:
                    m1[c] = 1
            for c in s2.toCharArray():
                if c in m2.keys():
                    m2[c] = m2[c] + 1
                else:
                    m2[c] = 1
            ans = 0
            hs = HashSet()
            for c in s2.toCharArray():
                if not hs.contains(c):
                    hs.add(c)
                    x1 = m1[c]
                    x2 = m2[c]
                    x1 = min(x1, x2)
                    ans += x1
            print(ans)
    @staticmethod
    def isValid(s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        map = {}
        for c in s1.toCharArray():
            map[c] = True
        for c in s2.toCharArray():
            if  c not in map.keys():
                return False
        return True
