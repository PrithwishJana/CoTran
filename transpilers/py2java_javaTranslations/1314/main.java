public void findSum ( n ) {
    var sum = 0;
    for i in range ( n ) :
        sum += i * ( n - i );
    return 2 * sum;
}
var n = 3;
System.out.println ( findSum ( n ) );
