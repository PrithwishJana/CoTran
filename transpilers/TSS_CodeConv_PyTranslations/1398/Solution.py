class Solution:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = Scanner(System.in)
        t = s.nextInt()
        m = s.nextInt()
        memory = [0 for _ in range(m)]
        allocIdx = 0
        for j in range(0, t):
            if s.next() is "alloc":
                n = s.nextInt()
                len = 0
                canAlloc = False
                for i in range(0, m):
                    if memory [i] == 0:
                        len += 1
                    else:
                        len = 0
                    if len == n:
                        canAlloc = True
                        len = i - n + 1
                        break
                if canAlloc:
                    allocIdx += 1
                    i = len
                    while i < len + n:
                        memory [i] = allocIdx
                        i += 1
                    print(allocIdx)
                else:
                    print("NULL")
            elif s.next() is "erase":
                x = s.nextInt()
                if x <= 0:
                    print("ILLEGAL_ERASE_ARGUMENT")
                    break
                hasErased = False
                for i in range(0, m):
                    if memory [i] == x:
                        memory [i] = 0
                        hasErased = True
                if not hasErased:
                    print("ILLEGAL_ERASE_ARGUMENT")
            elif s.next() is "defragment":
                d = 0
                for i in range(0, m):
                    if memory [i] == 0:
                        d += 1
                    else:
                        memory [i - d] = memory [i]
                for i in range(m - d, m):
                    memory [i] = 0
            else:
                print("h")
        s.close()
