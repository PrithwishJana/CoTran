class GFG:
    @staticmethod
    def towerOfHanoi(n, from_rod, to_rod, aux_rod1, aux_rod2):
        if n == 0:
            return
        if n == 1:
            print("Move disk " + str(n) + " from rod " + from_rod + " to rod " + to_rod)
            return
        GFG.towerOfHanoi(n - 2, from_rod, aux_rod1, aux_rod2, to_rod)
        print("Move disk " + str(n - 1) + " from rod " + from_rod + " to rod " + aux_rod2)
        print("Move disk " + str(n) + " from rod " + from_rod + " to rod " + to_rod)
        print("Move disk " + str(n - 1) + " from rod " + aux_rod2 + " to rod " + to_rod)
        GFG.towerOfHanoi(n - 2, aux_rod1, to_rod, from_rod, aux_rod2)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        GFG.towerOfHanoi(n, 'A', 'D', 'B', 'C')
