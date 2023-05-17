import math

class planet:
    FLIP = [0, 1, 5, - 1, - 1, 2, - 1, - 1, 8, - 1]
    @staticmethod
    def main(args):
        stdin = Scanner(System.in)
        nC = stdin.nextInt()
        for loop in range(0, nC):
            hr = stdin.nextInt()
            min = stdin.nextInt()
            tok = StringTokenizer(stdin.next(), ":")
            sHr = int(tok.nextToken())
            sMin = int(tok.nextToken())
            res = None
            i = sHr * min + sMin
            while i < hr * min:
                res = planet.flip(i, hr, min)
                if res is not None:
                    break
                i += 1
            if res is None:
                res = [0, 0, 0, 0]
            print("{0:d}{1:d}:{2:d}{3:d}\n".format(res [0], res [1], res [2], res [3]), end = '')
    @staticmethod
    def flip(val, hr, min):
        thisHr = math.trunc(val / float(min))
        thisMin = math.fmod(val, min)
        disp = [math.fmod(thisMin, 10), math.trunc(thisMin / float(10)), math.fmod(thisHr, 10), math.trunc(thisHr / float(10))]
        i = 0
        while i < len(disp):
            if planet.FLIP [disp [i]] == - 1:
                return None
            disp [i] = planet.FLIP [disp [i]]
            i += 1
        newHr = 10 * (disp [0]) + disp [1]
        newMin = 10 * (disp [2]) + disp [3]
        if newHr >= hr or newMin >= min:
            return None
        return [math.trunc(thisHr / float(10)), math.fmod(thisHr, 10), math.trunc(thisMin / float(10)), math.fmod(thisMin, 10)]
