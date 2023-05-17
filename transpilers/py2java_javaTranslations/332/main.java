public void ncr ( n , r ) {
    var ans = 1;
    for i in range ( 1 , r + 1 ) :
        ans *= ( n - r + i );
        ans //= i;
    return ans;
}
public void totalWays ( X , Y , M , W ) {
    return ( ncr ( M , X ) * ncr ( W , Y ) );
}
var X = 4;
var Y = 3;
var M = 6;
var W = 5;
System.out.println ( totalWays ( X , Y , M , W ) );
