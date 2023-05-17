import math

class cf1146B:
    @staticmethod
    def main(args):
        scan = Scanner(System.in)
        str = StringBuilder(scan.next())
        index = str.indexOf("a")
        aCnt = 0
        while index != - 1:
            aCnt += 1
            index = str.indexOf("a", index + 1)
        sLength = math.trunc((str.length() - aCnt) / float(2))
        s = str.substring(0, str.length() - sLength)
        s2 = s
        r = str.substring(str.length() - sLength)
        s = s.replaceAll("a", "")
        if s == r:
            print(s2)
        else:
            print(":(")
