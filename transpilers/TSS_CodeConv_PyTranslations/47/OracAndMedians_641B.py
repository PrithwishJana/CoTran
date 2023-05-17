class OracAndMedians_641B:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws NumberFormatException, IOException
    def main(args):
        br = BufferedReader(InputStreamReader(System.in))
        cases = int(br.readLine())
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (cases -- > 0)
        while cases  > 0:
            cases -= 1
            st = StringTokenizer(br.readLine())
            n = int(st.nextToken())
            target = int(st.nextToken())
            nums = [0 for _ in range(n)]
            st = StringTokenizer(br.readLine())
            for i in range(0, n):
                nums [i] = int(st.nextToken())
            OracAndMedians_641B._helper(nums, target)
        cases -= 1
    @staticmethod
    def _helper(nums, target):
        isTargetFound = False
        canPrintYes = False
        score = 0
        prev = - 1
        for num in nums:
            if num == target:
                isTargetFound = True
            if num < target:
                score -= 1
            else:
                score += 1
            if score > 0 and prev > - 1:
                canPrintYes = True
            prev = score
            score = max(score, 0)
        if (len(nums) == 1 or canPrintYes) and isTargetFound:
            print("yes")
        else:
            print("no")
