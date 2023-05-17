class A376_Lever_Round221:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        s = None
        s = sc.nextLine()
        sc.close()
        part = s.find("^")
        left = 0
        right = 0
        for i in range(0, part):
            if s[i] <= '9' and s[i] >= '1':
                left += (part - i) * (s[i] - '0')
        j = part + 1
        while j < len(s):
            if s[j] <= '9' and s[j] >= '1':
                right += (j - part) * (s[j] - '0')
            j += 1
        if left == right:
            print("balance")
        elif left < right:
            print("right")
        elif right < left:
            print("left")
