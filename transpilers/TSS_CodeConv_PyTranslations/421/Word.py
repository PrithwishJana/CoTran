class Word:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        word = in_.next()
        uppercase = 0
        lowercase = 0
        i = 0
        while i < len(word):
            ch = word[i]
            if ch.isupper():
                uppercase += 1
            else:
                lowercase += 1
            i += 1
        if uppercase > lowercase:
            print(word.upper())
        elif lowercase > uppercase:
            print(word.casefold())
        else:
            print(word.casefold())
