class Ex711B:
    @staticmethod
    def main(args):
        in_ = Scanner(System.in)
        n = in_.nextInt()
        magic_square = [[0 for _ in range(n)] for _ in range(n)]
        row = - 1
        column = - 1
        for i in range(0, n):
            for j in range(0, n):
                magic_square [i][j] = in_.nextInt()
                if magic_square [i][j] == 0:
                    row = i
                    column = j
        if n == 1:
            print(1)
            return
        sum = 0
        for i in range(0, n):
            if row != 0:
                sum += magic_square [0][i]
            else:
                sum += magic_square [1][i]
        answer = sum
        for i in range(0, n):
            answer -= magic_square [row][i]
        magic_square [row][column] = answer
        m = 0
        current_sumi = 0
        current_sumj = 0
        for i in range(0, n):
            for j in range(0, n):
                current_sumi += magic_square [i][j]
                current_sumj += magic_square [j][i]
            if current_sumi != sum or current_sumj != sum:
                m += 1
            current_sumi = 0
            current_sumj = 0
        for i in range(0, n):
            current_sumi += magic_square [i][i]
            current_sumj += magic_square [n - i - 1][i]
        if current_sumi != sum or current_sumj != sum:
            m += 1
        if m == 0 and answer > 0:
            print(answer)
        else:
            print(- 1)
