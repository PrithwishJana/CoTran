import math

#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static Math. *
class Exercise:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        landings = sc.nextInt()
        time = sc.nextInt()
        minutes = [0 for _ in range(landings)]
        for i in range(0, landings):
            hours = sc.nextInt() * 60
            minute = sc.nextInt()
            minutes [i] = minute + hours
        if time + 1 <= minutes [0]:
            print(str(0) + " " + str(0))
            return
        i = 0
        while i < landings - 1:
            if minutes [i + 1] - minutes [i] >= 2 * time + 2:
                flight = minutes [i] + time + 1
                h = math.trunc(flight / float(60))
                m = math.fmod(flight, 60)
                print(str(h) + " " + str(m))
                return
            i += 1
        flight = minutes [landings - 1] + time + 1
        h = math.trunc(flight / float(60))
        m = math.fmod(flight, 60)
        print(str(h) + " " + str(m))
