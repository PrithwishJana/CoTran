class GFG:
    @staticmethod
    def minReplacement(str):
        if len(str) > 26:
            print("IMPOSSIBLE")
        else:
            hash = [0 for _ in range(26)]
            i = 0
            while i < len(str):
                hash [str[i] - 'a'] += 1
                i += 1
            count = 0
            i = 0
            while i < len(str):
                if hash [str[i] - 'a'] > 1:
                    for j in range(0, 26):
                        if hash [j] == 0:
                            hash [str[i] - 'a'] -= 1
                            str = str[0:i] + chr((j + 'a')) + str[i + 1:]
                            hash [j] += 1
                            break
                i += 1
            print(str)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "xxxxyyyy"
        GFG.minReplacement(str)
