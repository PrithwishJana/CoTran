class GFG:
    @staticmethod
    def times(steps, n):
        current_level = 0
        previous_level = 0
        count = 0
        for i in range(0, n):
            previous_level = current_level
            current_level = current_level + steps [i]
            if (previous_level < 0 and current_level >= 0) or (previous_level > 0 and current_level <= 0):
                count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        steps = [1, - 1, 0, 0, 1, 1, - 3, 2]
        n = len(steps)
        print(GFG.times(steps, n))
