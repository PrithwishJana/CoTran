class GFG:
    @staticmethod
    def countCharacterType(str):
        vowels = 0
        consonant = 0
        specialChar = 0
        digit = 0
        i = 0
        while i < len(str):
            ch = str[i]
            if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
                ch = ch.casefold()
                pass
                if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
                    vowels += 1
                else:
                    consonant += 1
            elif ch >= '0' and ch <= '9':
                digit += 1
            else:
                specialChar += 1
            i += 1
        print("Vowels: " + str(vowels))
        print("Consonant: " + str(consonant))
        print("Digit: " + str(digit))
        print("Special Character: " + str(specialChar))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "geeks for geeks121"
        GFG.countCharacterType(str)
