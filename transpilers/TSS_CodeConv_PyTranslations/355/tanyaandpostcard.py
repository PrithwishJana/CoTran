class tanyaandpostcard:
    @staticmethod
    def main(args):
        in_ = Scanner(System.in)
        s1 = in_.nextLine()
        s2 = in_.nextLine()
        a = [0 for _ in range(123)]
        b = [0 for _ in range(len(s1))]
        i = 0
        y = 0
        w = 0
        ch = '\0'
        i = 0
        while i < len(s2):
            a [s2[i]] += 1
            i += 1
        i = 0
        while i < len(s1):
            ch = s1[i]
            if a [ch] >= 1:
                a [ch] -= 1
                b [i] = 1
                y += 1
            i += 1
        i = 0
        while i < len(s1):
            ch = s1[i]
            if b [i] == 0:
                if ch <= chr(90):
                    ch = chr((ord(ch) + 32))
                else:
                    ch = chr((ord(ch) - 32))
                if a [ch] >= 1:
                    a [ch] -= 1
                    w += 1
            i += 1
        print(str(y) + " " + str(w))
