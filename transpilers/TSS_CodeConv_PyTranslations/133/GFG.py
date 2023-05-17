class GFG:
    @staticmethod
    def reverseWords(str):
        st = Stack()
        i = 0
        while i < len(str):
            if str[i] != ' ':
                st.push(str[i])
            else:
                while st.empty() == False:
                    print(st.pop(), end = '')
                print(" ", end = '')
            i += 1
        while st.empty() == False:
            print(st.pop(), end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "Geeks for Geeks"
        GFG.reverseWords(str)
