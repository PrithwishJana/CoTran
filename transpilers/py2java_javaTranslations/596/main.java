class Solution extends  object {
    public void minMoves ( this , nums ) {
        if (nums is None or len ( nums ) == 0) {
            return 0;
        }
         var min_num = min ( nums );
        return sum ( { i - min_num for i in nums } );
    }
}

if (var __name__ == "__main__") {
    var sObj = Solution ( );
    var nums = { 1 , 2 , 3 };
    var out = sObj . minMoves ( nums );
    System.out.println ( out );
}
 