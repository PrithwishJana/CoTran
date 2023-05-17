public void nCr ( n , r ) {
    var fac = list ( );
    fac . append ( 1 );
    for i in range ( 1 , n + 1 ) :
        fac . append ( fac { i - 1 } * i );
    var ans = fac { n } / ( fac { n - r } * fac { r } );
    return ans;
}
n = 3;
k = 3;
ans = nCr ( n + k - 1 , k ) + nCr ( k - 1 , n - 1 );
System.out.println ( ans );
