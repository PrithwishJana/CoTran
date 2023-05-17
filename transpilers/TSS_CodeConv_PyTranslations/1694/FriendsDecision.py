class FriendsDecision:
    count = 0
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        n = sc.nextInt()
        sc.nextLine()
        arr = [None for _ in range(n)]
        for i in range(0, n):
            arr [i] = sc.nextLine()
            FriendsDecision._decision(arr [i])
        print(FriendsDecision.count)
    @staticmethod
    def _decision(entery):
        localct = 0
        inputs = entery.split(" ")
        i = 0
        while i < len(inputs):
            if inputs [i] == "1":
                localct += 1
            i += 1
        if localct > 1:
            FriendsDecision.count += 1
