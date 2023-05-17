public void seriessum ( n ) {
    var sum = 0;
    for i in range ( 1 , n + 1 ) :
        sum += i * ( i + 1 ) / 2;
    return sum;
}
var n = 4;
System.out.println ( seriessum ( n ) );
