import math

class p222:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self._sphereRadii = None
        self._minLength = None

    @staticmethod
    def main(args):
        print((p222()).run())
    def run(self):
        self._sphereRadii = [0 for _ in range(21)]
        i = 0
        while i < len(self._sphereRadii):
            self._sphereRadii [i] = (i + 30) * 1000
            i += 1
        self._minLength = [[0 for _ in range(1 << len(self._sphereRadii))] for _ in range(len(self._sphereRadii))]
        min = Double.POSITIVE_INFINITY
        i = 0
        while i < len(self._sphereRadii):
            min = min(self._findMinimumLength(i, (1 << len(self._sphereRadii)) - 1) + self._sphereRadii [i], min)
            i += 1
        return str(round(min))
    def _findMinimumLength(self, currentSphereIndex, setOfSpheres):
        if (setOfSpheres & (1 << currentSphereIndex)) == 0:
            raise IllegalArgumentException()
        if self._minLength [currentSphereIndex][setOfSpheres] == 0:
            result = 0
            if Integer.bitCount(setOfSpheres) == 1:
                result = self._sphereRadii [currentSphereIndex]
            else:
                result = Double.POSITIVE_INFINITY
                newSetOfSpheres = setOfSpheres ^ (1 << currentSphereIndex)
                i = 0
                while i < len(self._sphereRadii):
                    if (newSetOfSpheres & (1 << i)) == 0:
                        i += 1
                        continue
                    temp = math.sqrt((self._sphereRadii [i] + self._sphereRadii [currentSphereIndex] - 50000) * 200000)
                    temp += self._findMinimumLength(i, newSetOfSpheres)
                    result = min(temp, result)
                    i += 1
            self._minLength [currentSphereIndex][setOfSpheres] = result
        return self._minLength [currentSphereIndex][setOfSpheres]
