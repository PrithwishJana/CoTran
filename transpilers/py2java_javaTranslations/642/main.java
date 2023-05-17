public void multiplyWith3Point5 ( x ) {
    return ( x << 1 ) + x + ( x >> 1 );
}
var x = 4;
System.out.println ( multiplyWith3Point5 ( x ) );
