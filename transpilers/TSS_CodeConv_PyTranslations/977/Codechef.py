import math

class Codechef:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.lang.Exception
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        try:
            sc = Scanner(System.in)
            t = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
            while t  > 0:
                t -= 1
                s = sc.next()
                ch = s.toCharArray()
                i = 0
                while i < len(ch):
                    if math.fmod((i + 1), 2) != 0:
                        if ch [i] != 'a':
                            ch [i] = 'a'
                        else:
                            ch [i] = 'b'
                    elif math.fmod((i + 1), 2) == 0:
                        if ch [i] != 'z':
                            ch [i] = 'z'
                        else:
                            ch [i] = 'y'
                    i += 1
                s = str(ch)
                print(s)
            t -= 1
        except Exception as e:
            pass
