public void firstSetBit ( n ) {
    var x = n & ( n - 1 );
    return ( n ^ x );
}
var n = 12;
System.out.println ( firstSetBit ( n ) );
