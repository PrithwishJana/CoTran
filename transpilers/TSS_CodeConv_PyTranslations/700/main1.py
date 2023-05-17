class main1:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        arr = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(0, 4):
            for j in range(0, 4):
                arr [i][j] = sc.nextInt()
        if arr [0][3] == 1:
            if arr [0][1] == 1 or arr [0][2] == 1 or arr [0][0] == 1 or arr [1][0] == 1 or arr [2][1] == 1 or arr [3][2] == 1:
                print("YES")
                return
        if arr [1][3] == 1:
            if arr [1][1] == 1 or arr [1][2] == 1 or arr [1][0] == 1 or arr [2][0] == 1 or arr [3][1] == 1 or arr [0][2] == 1:
                print("YES")
                return
        if arr [2][3] == 1:
            if arr [2][1] == 1 or arr [2][2] == 1 or arr [2][0] == 1 or arr [3][0] == 1 or arr [0][1] == 1 or arr [1][2] == 1:
                print("YES")
                return
        if arr [3][3] == 1:
            if arr [3][1] == 1 or arr [3][2] == 1 or arr [3][0] == 1 or arr [0][0] == 1 or arr [1][1] == 1 or arr [2][2] == 1:
                print("YES")
                return
        print("NO")
