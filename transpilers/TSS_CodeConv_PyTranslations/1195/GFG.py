class GFG:
    @staticmethod
    def findMaxGuests(arrl, exit, n):
        Arrays.sort(arrl)
        Arrays.sort(exit)
        guests_in = 1
        max_guests = 1
        time = arrl [0]
        i = 1
        j = 0
        while i < n and j < n:
            if arrl [i] <= exit [j]:
                guests_in += 1
                if guests_in > max_guests:
                    max_guests = guests_in
                    time = arrl [i]
                i += 1
            else:
                guests_in -= 1
                j += 1
        print("Maximum Number of Guests = " + str(max_guests) + " at time " + str(time))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arrl = [1, 2, 10, 5, 5]
        exit = [4, 5, 12, 9, 12]
        n = len(arrl)
        GFG.findMaxGuests(arrl, exit, n)
