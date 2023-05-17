public void isKthBitSet ( n , k ) {
    if (( ( n >> ( k - 1 ) ) & 1 )) {
        return true;
    }
     return false;
}
public void setKthBit ( n , k ) {
    return ( ( 1 << ( k - 1 ) ) | n );
}
public void allBitsAreSet ( n ) {
    if (( ( ( n + 1 ) & n ) == 0 )) {
        return true;
    }
     return false;
}
public void bitsAreInAltOrder ( n ) {
    var num = n ^ ( n >> 1 );
    return allBitsAreSet ( num );
}
public void bitsAreInAltPatrnInGivenRange ( n , l , r ) {
    if (( isKthBitSet ( n , r ) )) {
        num = n;
        left_shift = r;
    }
     else{
        num = setKthBit ( n , ( r + 1 ) );
        left_shift = r + 1;
    }
    num = num & ( ( 1 << left_shift ) - 1 );
    num = num >> ( l - 1 );
    return bitsAreInAltOrder ( num );
}
if (var __name__ == '__main__') {
    var n = 18;
    var l = 1;
    var r = 3;
    if (( bitsAreInAltPatrnInGivenRange ( n , l , r ) )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
}
 