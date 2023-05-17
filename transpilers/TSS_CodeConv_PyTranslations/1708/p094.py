import math

class p094:
    @staticmethod
    def main(args):
        print((p094()).run())
    _LIMIT = Library.pow(10, 9)
    def run(self):
        sum = 0
        s = 1
        while s * s <= math.trunc((p094._LIMIT + 1) / float(3)):
            for t in range(s - 2, 0, -2):
                if Library.gcd(s, t) == 1:
                    a = s * t
                    b = math.trunc((s * s - t * t) / float(2))
                    c = math.trunc((s * s + t * t) / float(2))
                    if a * 2 == c - 1:
                        p = c * 3 - 1
                        if p <= p094._LIMIT:
                            sum += p
                    if a * 2 == c + 1:
                        p = c * 3 + 1
                        if p <= p094._LIMIT:
                            sum += p
                    if b * 2 == c - 1:
                        p = c * 3 - 1
                        if p <= p094._LIMIT:
                            sum += p
                    if b * 2 == c + 1:
                        p = c * 3 + 1
                        if p <= p094._LIMIT:
                            sum += p
            s += 2
        return str(sum)
