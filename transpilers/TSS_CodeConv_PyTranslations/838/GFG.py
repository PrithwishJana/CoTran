class GFG:
    @staticmethod
    def areElementsContiguous(arr, n):
        us = HashSet()
        for i in range(0, n):
            us.add(arr [i])
        count = 1
        curr_ele = arr [0] - 1
        while us.contains(curr_ele) == True:
            count += 1
            curr_ele -= 1
        curr_ele = arr [0] + 1
        while us.contains(curr_ele) == True:
            count += 1
            curr_ele += 1
        return (count == (us.size()))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [5, 2, 3, 6, 4, 4, 6, 6]
        n = len(arr)
        if GFG.areElementsContiguous(arr, n):
            print("Yes")
        else:
            print("No")
