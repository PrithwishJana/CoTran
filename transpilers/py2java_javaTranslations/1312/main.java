public void squareSum ( n ) {
    var sum = 0;
    for i in range ( 0 , n + 1 ) :
        sum += ( 2 * i ) * ( 2 * i );
    return sum;
}
var ans = squareSum ( 8 );
System.out.println ( ans );
