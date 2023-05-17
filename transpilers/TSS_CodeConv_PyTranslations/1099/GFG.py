class GFG:
    @staticmethod
    def checkStackPermutation(ip, op, n):
        input = java.util.LinkedList()
        for i in range(0, n):
            input.add(ip [i])
        output = java.util.LinkedList()
        for i in range(0, n):
            output.add(op [i])
        tempStack = java.util.Stack()
        while not input.isEmpty():
            ele = input.poll()
            if ele == output.peek():
                output.poll()
                while not tempStack.isEmpty():
                    if tempStack.peek() == output.peek():
                        tempStack.pop()
                        output.poll()
                    else:
                        break
            else:
                tempStack.push(ele)
        return (input.isEmpty() and tempStack.isEmpty())
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        input = [1, 2, 3]
        output = [2, 1, 3]
        n = 3
        if GFG.checkStackPermutation(input, output, n):
            print("Yes")
        else:
            print("Not Possible")
