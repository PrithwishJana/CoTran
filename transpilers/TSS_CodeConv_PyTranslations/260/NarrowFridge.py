class NarrowFridge:
    _s = Scanner(System.in)
    @staticmethod
    def main(args):
        n = NarrowFridge._s.nextInt()
        h = NarrowFridge._s.nextInt()
        arr = [0 for _ in range(n)]
        for i in range(0, n):
            arr [i] = NarrowFridge._s.nextInt()
        overAllPq = PriorityQueue(Collections.reverseOrder())
        ans = - 1
        for i in range(0, n):
            overAllPq.add(arr [i])
            pq = PriorityQueue(Collections.reverseOrder())
            pq.addAll(overAllPq)
            c1 = h
            c2 = h
            flag = True
            while not pq.isEmpty():
                if flag:
                    if c1 >= pq.peek():
                        c1 -= pq.poll()
                    else:
                        break
                    flag = False
                else:
                    if c2 >= pq.peek():
                        c2 -= pq.poll()
                    else:
                        break
                    flag = True
            if pq.isEmpty():
                ans = i + 1
            else:
                break
        print(ans)
        NarrowFridge._s.close()
