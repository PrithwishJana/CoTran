var mod = 1000000007;
public void fact ( n ) {
    var res = 1;
    for i in range ( 2 , n + 1 ) :
        res = res * i;
    return res;
}
public void nCr ( n , r ) {
    return int ( fact ( n ) / ( fact ( r ) * fact ( n - r ) ) );
}
public void powmod ( a , n ) {
    if (( var n == 0 )) {
        return 1;
    }
     pt = powmod ( a , int ( n / 2 ) );
    pt = ( pt * pt ) % mod;
    if (( n % 2 )) {
        return ( pt * a ) % mod;
    }
     else{
        return pt;
    }
}
public void CountSubset ( arr , n ) {
    ans = powmod ( 2 , n - 1 );
    arr . sort ( reverse = false );
    for i in range ( n ) :
        j = i + 1;
        while (( j < n and arr { j } == arr { i } )) {
            r = n - 1 - j;
            l = i;
            ans = ( ans + nCr ( l + r , l ) ) % mod;
            j += 1;
        }
     return ans;
}
if (__name__ == '__main__') {
    arr = { 2 , 3 , 2 };
    n = len ( arr );
    System.out.println ( CountSubset ( arr , n ) );
}
 