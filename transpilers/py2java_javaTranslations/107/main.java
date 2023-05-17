public void countSetBits ( n ) {
    var bitCount = 0;
    for i in range ( 1 , n + 1 ) :
        bitCount += countSetBitsUtil ( i );
    return bitCount;
}
public void countSetBitsUtil ( x ) {
    if (( x <= 0 )) {
        return 0;
    }
     return ( 0 if int ( x % 2 ) == 0 else 1 ) + countSetBitsUtil ( int ( x / 2 ) );
}
if (var __name__ == '__main__') {
    var n = 4;
    System.out.println ( "Total set bit count is" , countSetBits ( n ) );
}
 