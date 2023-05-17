class InterceptedMessage:
    @staticmethod
    def main(args):
        scanner = java.util.Scanner(System.in)
        totalFirstFiles = scanner.nextInt()
        totalSecondFiles = scanner.nextInt()
        firstFiles = [0 for _ in range(totalFirstFiles)]
        secondFiles = [0 for _ in range(totalSecondFiles)]
        for i in range(0, totalFirstFiles):
            firstFiles [i] = scanner.nextInt()
        for i in range(0, totalSecondFiles):
            secondFiles [i] = scanner.nextInt()
        print(InterceptedMessage._interceptedMessage(firstFiles, secondFiles))
    @staticmethod
    def _interceptedMessage(firstFiles, secondFiles):
        maxFiles = 0
        firstPointer = 0
        secondPointer = 0
        hasFinished = False
        tempFirstNumber = 0
        tempSecondNumber = 0
        while not hasFinished:
            if firstPointer == 0 and secondPointer == 0:
                tempFirstNumber += firstFiles [firstPointer]
                tempSecondNumber += secondFiles [secondPointer]
            if tempFirstNumber == tempSecondNumber:
                maxFiles += 1
                firstPointer += 1
                secondPointer += 1
                if firstPointer > len(firstFiles) - 1 and secondPointer > len(secondFiles) - 1:
                    break
                tempFirstNumber = firstFiles [firstPointer]
                tempSecondNumber = secondFiles [secondPointer]
            elif tempFirstNumber < tempSecondNumber:
                firstPointer += 1
                tempFirstNumber += firstFiles [firstPointer]
            else:
                secondPointer += 1
                tempSecondNumber += secondFiles [secondPointer]
        return maxFiles
