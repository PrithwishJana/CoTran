public void toggleBitsFromLToR ( n , l , r ) {
    var num = ( ( ( 1 << r ) - 1 ) ^ ( ( 1 << ( l - 1 ) ) - 1 ) );
    return ( n ^ num );
}
public void unsetBitsInGivenRange ( n , l , r ) {
    num = ( 1 << ( 4 * 8 - 1 ) ) - 1;
    num = toggleBitsFromLToR ( num , l , r );
    return ( n & num );
}
var n = 42;
var l = 2;
var r = 5;
System.out.println ( unsetBitsInGivenRange ( n , l , r ) );
