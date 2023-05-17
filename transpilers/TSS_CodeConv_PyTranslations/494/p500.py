import math

class p500:
    @staticmethod
    def main(args):
        print((p500()).run())
    _TARGET = 500500
    _MODULUS = 500500507
    def run(self):
        queue = java.util.PriorityQueue()
        nextPrime = 2
        queue.add(int(nextPrime))
        product = 1
        for i in range(0, p500._TARGET):
            item = queue.remove()
            product *= math.fmod(item, p500._MODULUS)
            product = math.fmod(product, p500._MODULUS)
            queue.add(item * item)
            if item == nextPrime:
                loop_condition = True
                while loop_condition:
                    nextPrime += 1
                    loop_condition = not Library.isPrime(nextPrime)
                queue.add(int(nextPrime))
        return str(product)
