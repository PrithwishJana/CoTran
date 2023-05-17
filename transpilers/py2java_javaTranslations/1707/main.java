class Solution extends  object {
    public void isToeplitzMatrix ( this , matrix ) {
        for r in range ( len ( matrix ) - 1 ) :
            for c in range ( len ( matrix { 0 } ) - 1 ) :
                if (matrix { r } { c } != matrix { r + 1 } { c + 1 }) {
                    return false;
                }
         return true;
    }
}

if (var __name__ == "__main__") {
    var sObj = Solution ( );
    var matrix = { [ 1 , 2 , 3 , 4 } , { 5 , 1 , 2 , 3 } , { 9 , 5 , 1 , 2 } ];
    var out = sObj . isToeplitzMatrix ( matrix );
    System.out.println ( out );
}
 