class B629:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        n = sc.nextInt()
        FfriendPerDay = [0 for _ in range(367)]
        MfriendPerDay = [0 for _ in range(367)]
        answer = 0
        for i in range(0, n):
            c = sc.next().charAt(0)
            a = sc.nextInt()
            b = sc.nextInt()
            for j in range(a, b + 1):
                if c == 'M':
                    MfriendPerDay [j] += 1
                else:
                    FfriendPerDay [j] += 1
                if MfriendPerDay [j] < FfriendPerDay [j]:
                    if MfriendPerDay [j] > answer:
                        answer = MfriendPerDay [j]
                else:
                    if FfriendPerDay [j] > answer:
                        answer = FfriendPerDay [j]
        print(answer * 2)
