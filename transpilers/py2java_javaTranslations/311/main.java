public void countSquares ( n ) {
    return ( ( n * ( n + 1 ) / 2 ) * ( 2 * n + 1 ) / 3 );
}
var n = 3;
System.out.println ( "Count of squares is" , int ( countSquares ( n ) ) );
