class ShortestKingPath:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        s = in_.next()
        s1 = in_.next()
        c = s.toCharArray()
        c1 = s1.toCharArray()
        diff = c1 [0] - c [0]
        dif = c1 [1] - c [1]
        n = abs(diff)
        m = abs(dif)
        ans = ""
        while diff != 0 or dif != 0:
            if diff > 0:
                ans += "R"
                diff -= 1
            if diff < 0:
                ans += "L"
                diff += 1
            if dif > 0:
                ans += "U"
                dif -= 1
            if dif < 0:
                ans += "D"
                dif += 1
            ans += "\n"
        print(max(n, m))
        print(ans)
