class GFG:
    @staticmethod
    def charCheck(input_char):
        if (input_char >= chr(65) and input_char <= chr(90)) or (input_char >= chr(97) and input_char <= chr(122)):
            print(" Alphabet ")
        elif input_char >= chr(48) and input_char <= chr(57):
            print(" Digit ")
        else:
            print(" Special Character ")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        input_char = '$'
        GFG.charCheck(input_char)
