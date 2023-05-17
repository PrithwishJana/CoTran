class Punctuation:
    @staticmethod
    def isLatinLetter(c):
        return c >= 'a' and c <= 'z'
    @staticmethod
    def isPunctuation(c):
        if c == '.':
            return True
        if c == ',':
            return True
        if c == '!':
            return True
        if c == '?':
            return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.io.IOException
    def main(args):
        br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        pw = java.io.PrintWriter(System.out)
        s = br.readLine()
        sb = StringBuilder()
        n = len(s)
        sb.append(s[0])
        for i in range(1, n):
            c = s[i]
            if Punctuation.isLatinLetter(c):
                if not Punctuation.isLatinLetter(s[i - 1]):
                    sb.append(' ')
                sb.append(c)
            elif Punctuation.isPunctuation(c):
                sb.append(c)
        pw.println(sb)
        pw.flush()
        pw.close()
