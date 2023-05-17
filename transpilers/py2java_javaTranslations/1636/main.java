class Solution extends  object {
    public void checkPossibility ( this , nums ) {
        var broken_num = 0;
        for i in range ( len ( nums ) - 1 ) :
            if (( nums { i } > nums { i + 1 } )) {
                broken_num += 1;
                if (broken_num >= 2) {
                    return false;
                }
                 if (( i - 1 < 0 or nums { i - 1 } <= nums { i + 1 } )) {
                    nums { i } = nums { i + 1 };
                }
                 else{
                    nums { i + 1 } = nums { i };
                }
            }
         return true;
    }
}

if (var __name__ == "__main__") {
    var sObj = Solution ( );
    var nums = { 4 , 2 , 3 };
    var out = sObj . checkPossibility ( nums );
    System.out.println ( out );
}
 