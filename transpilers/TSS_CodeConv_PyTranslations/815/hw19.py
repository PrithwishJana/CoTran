import math

class hw19:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
    def main(args):
        scan = Scanner(System.in)
            in_ = scan.next()
            i = int(str(in_[len(in_) - 1]))
            if len(in_) > 1 and math.fmod((int(str(in_[len(in_) - 2])) * 10 + i), 4) == 0:
                print(4)
            elif len(in_) == 1 and math.fmod(i, 4) == 0:
                print(4)
            else:
                print(0)
