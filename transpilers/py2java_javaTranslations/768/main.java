class Solution extends  object {
    public void maxAreaOfIsland ( this , grid ) {
        var ans = 0;
        for i in range ( len ( grid ) ) :
            for j in range ( len ( grid { 0 } ) ) :
                if (grid { i } { j } == 1) {
                    grid { i } { j } = 0;
                    ans = max ( this . dfs ( grid , i , j ) , ans );
                }
         return ans;
    }
    public void dfs ( this , grid , i , j ) {
        var stack = { ( i , j ) };
        var area = 0;
        while (stack) {
            r , var c = stack . pop ( - 1 );
            area += 1;
            for nr , nc in ( ( r - 1 , c ) , ( r + 1 , c ) , ( r , c - 1 ) , ( r , c + 1 ) ) :
                if (( 0 <= nr < len ( grid ) and 0 <= nc < len ( grid { 0 } ) and grid { nr } { nc } )) {
                    stack . append ( ( nr , nc ) );
                    grid { nr } { nc } = 0;
                }
         }
         return area;
    }
}

if (var __name__ == "__main__") {
    var sObj = Solution ( );
    var grid = { [ 0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 } , { 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 } , { 0 , 1 , 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 } , { 0 , 1 , 0 , 0 , 1 , 1 , 0 , 0 , 1 , 0 , 1 , 0 , 0 } , { 0 , 1 , 0 , 0 , 1 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 0 } , { 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 } , { 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 } , { 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 } ];
    var out = sObj . maxAreaOfIsland ( grid );
    System.out.println ( out );
}
 