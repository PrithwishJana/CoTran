public void findSum ( n ) {
    n -= 1;
    var sum = 0;
    sum += ( n * ( n + 1 ) ) / 2;
    sum += ( n * ( n + 1 ) * ( 2 * n + 1 ) ) / 6;
    return int ( sum );
}
var n = 3;
System.out.println ( findSum ( n ) );
