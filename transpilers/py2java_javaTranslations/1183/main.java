public void TotalWays ( n , s , k ) {
    var dp = { 0 } * n;
    dp { s - 1 } = 1;
    for i in range ( s , n ) :
        var idx = max ( s - 1 , i - k );
        for j in range ( idx , i ) :
            dp { i } += dp { j };
    return dp { n - 1 };
}
if (var __name__ == "__main__") {
    var n = 5;
    var k = 2;
    var s = 2;
    System.out.println ( "Total Ways = " , TotalWays ( n , s , k ) );
}
 