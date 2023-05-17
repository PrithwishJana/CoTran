public void grayCode ( n ) {
    return n ^ ( n >> 1 );
}
var n = 10;
System.out.println ( grayCode ( n ) );
