import math

class p019:
    @staticmethod
    def main(args):
        print((p019()).run())
    def run(self):
        count = 0
        for y in range(1901, 2001):
            for m in range(1, 13):
                if p019._dayOfWeek(y, m, 1) == 0:
                    count += 1
        return str(count)
    @staticmethod
    def _dayOfWeek(year, month, day):
        if year < 0 or year > 10000 or month < 1 or month > 12 or day < 1 or day > 31:
            raise IllegalArgumentException()
        m = math.fmod((month - 3 + 4800), 4800)
        y = math.fmod((year + math.trunc(m / float(12))), 400)
        m = math.fmod(m, 12)
        return math.fmod((y + math.trunc(y / float(4)) - math.trunc(y / float(100)) + math.trunc((13 * m + 2) / float(5)) + day + 2), 7)
