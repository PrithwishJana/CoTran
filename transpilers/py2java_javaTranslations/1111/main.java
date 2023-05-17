public void countWays ( n ) {
    var dp = { 0 for i in range ( n + 1 ) };
    dp { 0 } = 0;
    dp { 1 } = 1;
    dp { 2 } = 1;
    for i in range ( 3 , n + 1 ) :
        dp { i } = dp { i - 1 } + dp { i - 3 } + 1;
    return dp { n };
}
var n = 6;
System.out.println ( countWays ( n ) );
