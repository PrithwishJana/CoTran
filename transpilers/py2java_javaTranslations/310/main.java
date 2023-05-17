global maxn;
var maxn = 16;
public void precompute ( ) {
    var dp = { - 1 for i in range ( maxn ) };
    dp { 0 } = 0;
    v = { 4 , 6 , 9 };
    for i in range ( 1 , maxn , 1 ) :
        for k in range ( 3 ) :
            j = v { k };
            if (( i >= j and dp { i - j } != - 1 )) {
                dp { i } = max ( dp { i } , dp { i - j } + 1 );
            }
     return dp;
}
public void Maximum_Summands ( dp , n ) {
    if (( n < maxn )) {
        return dp { n };
    }
     else{
        t = int ( ( n - maxn ) / 4 ) + 1;
        return t + dp { n - 4 * t };
    }
}
if (__name__ == '__main__') {
    n = 12;
    dp = precompute ( );
    System.out.println ( Maximum_Summands ( dp , n ) );
}
 