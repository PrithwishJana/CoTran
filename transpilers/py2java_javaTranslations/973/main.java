var dp = { [ [ - 1 for i in range ( 5 ) } for i in range ( 501 ) ] for i in range ( 501 ) ];
public void countWaysUtil ( n , parts , nextPart ) {
    if (( var parts == 0 and n == 0 )) {
        return 1;
    }
     if (( n <= 0 or parts <= 0 )) {
        return 0;
    }
     if (( dp { n } { nextPart } { parts } != - 1 )) {
        return dp { n } { nextPart } { parts };
    }
     var ans = 0;
    for i in range ( nextPart , n + 1 ) :
        ans += countWaysUtil ( n - i , parts - 1 , i );
    dp { n } { nextPart } { parts } = ans;
    return ( ans );
}
public void countWays ( n ) {
    return countWaysUtil ( n , 4 , 1 );
}
var n = 8;
System.out.println ( countWays ( n ) );
