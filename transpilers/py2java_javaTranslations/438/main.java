public void minimumCost ( cost , n ) {
    var dp1 = 0;
    dp2 = 0;
    for i in range ( n ) :
        dp0 = cost { i } + min ( dp1 , dp2 );
        dp2 = dp1;
        dp1 = dp0;
    return min ( dp1 , dp2 );
}
if (var __name__ == "__main__") {
    var a = { 2 , 5 , 3 , 1 , 7 , 3 , 4 };
    var n = len ( a );
    System.out.println ( minimumCost ( a , n ) );
}
 