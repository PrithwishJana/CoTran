class AlternatingCurrent:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.io.IOException
    def main(args):
        br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        in_ = br.readLine().trim().toCharArray()
        stk = java.util.Stack()
        for c in in_:
            if stk.isEmpty():
                stk.push(c)
                continue
            top = stk.peek()
            if top == c:
                stk.pop()
            else:
                stk.push(c)
        if stk.isEmpty():
            print("Yes")
        else:
            print("No")
