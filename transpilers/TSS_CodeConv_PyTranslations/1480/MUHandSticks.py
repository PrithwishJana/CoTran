class MUHandSticks:
    @staticmethod
    def main(args):
        s = java.util.Scanner(System.in)
        sticks = [0 for _ in range(9)]
        for i in range(0, 6):
            sticks [s.nextInt() - 1] += 1
        legs = False
        headbody = False
        for i in range(0, 9):
            if sticks [i] >= 4:
                legs = True
            if sticks [i] >= 6:
                headbody = True
            if sticks [i] == 2:
                headbody = True
        if legs and headbody:
            print("Elephant")
        elif legs:
            print("Bear")
        else:
            print("Alien")
