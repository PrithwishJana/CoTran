public void AvgofSquareN ( n ) {
    var sum = 0;
    for i in range ( 1 , n + 1 ) :
        sum += ( i * i );
    return sum / n;
}
var n = 2;
System.out.println ( AvgofSquareN ( n ) );
