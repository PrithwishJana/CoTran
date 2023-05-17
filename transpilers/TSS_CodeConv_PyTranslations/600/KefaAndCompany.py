class KefaAndCompany:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
    def main(args):
        br = BufferedReader(InputStreamReader(System.in))
        str = br.readLine().trim().split(" ")
        n = int(str [0])
        k = int(str [1])
        pf = [0 for _ in range(n)]
        list = []
        for i in range(0, n):
            input = br.readLine().trim().split(" ")
            money = int(input [0])
            friend = int(input [1])
            list.append(Kefa(money, friend))
        Collections.sort(list, KefaCmp())
        ans = 0
        s = 0
        e = 0
        sum = 0
        while e < n:
            if list[e].money - list[s].money < k:
                sum += list[e].friend
                e += 1
            else:
                sum -= list[s].friend
                s += 1
            ans = max(ans, sum)
        print(ans)
class Kefa:
    def __init__(self, money, friend):
        #instance fields found by Java to Python Converter:
        self.money = 0
        self.friend = 0

        self.money = money
        self.friend = friend
class KefaCmp(Comparator):
    def compare(self, o1, o2):
        return o1.money - o2.money
