import math;
public void fourthPowerSum ( n ) {
    var sum = 0;
    for i in range ( 1 , n + 1 ) :
        sum = sum + ( i * i * i * i );
    return sum;
}
var n = 6;
System.out.println ( fourthPowerSum ( n ) );
