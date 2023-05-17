class C:
    _in_ = Scanner(System.in)
    @staticmethod
    def main(args):
        C = C._in_.nextInt()
        for thisCase in range(1, C + 1):
#JAVA TO PYTHON CONVERTER TASK: The following line has a Java format specifier which cannot be directly translated to Python:
            print("Case #{0:d}: {1:d}%n".format(thisCase, C._largestCircle()), end = '')
    @staticmethod
    def _largestCircle():
        N = C._in_.nextInt()
        bff = [0 for _ in range(N)]
        for i in range(0, N):
            bff [i] = C._in_.nextInt() - 1
        status = [0 for _ in range(N)]
        chainLength = [0 for _ in range(N)]
        for i in range(0, N):
            status [i] = - 2
            chainLength [i] = 0
        for i in range(0, N):
            if bff [bff [i]] == i:
                status [i] = - 1
        maxLoopSize = 0
        for i in range(0, N):
            if status [i] != - 1:
                current = bff [i]
                status [i] = i
                steps = 1
                done = False
                while not done:
                    if current == i:
                        if steps > maxLoopSize:
                            maxLoopSize = steps
                        done = True
                    elif status [current] == i:
                        done = True
                    elif status [current] == - 1:
                        if steps > chainLength [current]:
                            chainLength [current] = steps
                        done = True
                    else:
                        steps += 1
                        status [current] = i
                        current = bff [current]
        frankenCircle = 0
        for i in range(0, N):
            if status [i] == - 1:
                frankenCircle += (chainLength [i] + 1)
        return max(frankenCircle, maxLoopSize)
