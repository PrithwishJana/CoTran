class DeleteN:
    @staticmethod
    def main(args):
        in_ = 1234
        inp = str(in_)
        del_ = 3
        print("num_after_deleting_from_starting " + DeleteN.fromStart(inp, del_))
        print("num_after_deleting_from_ending " + DeleteN.fromEnd(inp, del_))
    @staticmethod
    def fromStart(inp, del_):
        try:
            inp1 = inp[0:del_ - 1]
            inp2 = inp[del_:len(inp)]
            return inp1 + inp2
        except Exception as e:
            return "Check Input"
    @staticmethod
    def fromEnd(inp, del_):
        try:
            inp1 = inp[0:len(inp) - del_]
            inp2 = inp[len(inp) - del_ + 1:len(inp)]
            return inp1 + inp2
        except Exception as e:
            return "Check Input"
