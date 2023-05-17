class FileName:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        n = sc.nextInt()
        str = sc.next()
        count = 0
        total = 0
        i = 0
        while i < len(str):
            if str[i] == 'x':
                count += 1
                i += 1
                continue
            else:
                if count >= 3:
                    total += count - 2
                    count = 0
                count = 0
            i += 1
        if count >= 3:
            total += count - 2
            count = 0
        print(total)
