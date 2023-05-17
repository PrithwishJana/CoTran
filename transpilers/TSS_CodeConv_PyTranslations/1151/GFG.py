import math

class GFG:
    @staticmethod
    def findMinimumX(a, n):
        st = java.util.HashSet()
        for i in range(0, n):
            st.add(a [i])
        if st.size() == 1:
            return 0
        if st.size() == 2:
            it = st.iterator()
            el1 = it.next()
            el2 = it.next()
            if math.fmod((el2 - el1), 2) == 0:
                return math.trunc((el2 - el1) / float(2))
            else:
                return (el2 - el1)
        if st.size() == 3:
            it = st.iterator()
            el1 = it.next()
            el2 = it.next()
            el3 = it.next()
            if (el2 - el1) == (el3 - el2):
                return el2 - el1
            else:
                return - 1
        return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [1, 4, 4, 7, 4, 1]
        n = len(a)
        print(GFG.findMinimumX(a, n))
