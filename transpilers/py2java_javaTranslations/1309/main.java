import math;
public void sumOfSeries ( n ) {
    var sum = 0;
    for i in range ( 1 , n + 1 ) :
        sum = sum + ( 2 * i - 1 ) * ( 2 * i - 1 );
    return sum;
}
var n = 10;
System.out.println ( sumOfSeries ( n ) );
