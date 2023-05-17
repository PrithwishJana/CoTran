class c1029A:
    @staticmethod
    def main(args):
        scan = java.util.Scanner(System.in)
        n = scan.nextInt()
        k = scan.nextInt()
        s = scan.next()
        ans = 0
        i = 1
        while i < len(s):
            if s[0:i] is s[len(s) - i:]:
                ans = i
            i += 1
        sb = StringBuilder()
        sb.append(s[len(s) - ans:])
        for i in range(0, k):
            sb.append(s[ans:])
        print(sb)
