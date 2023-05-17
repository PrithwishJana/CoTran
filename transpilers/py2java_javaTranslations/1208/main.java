import math;
public void fourthPowerSum ( n ) {
    return ( ( 6 * n * n * n * n * n ) + ( 15 * n * n * n * n ) + ( 10 * n * n * n ) - n ) / 30;
}
var n = 6;
System.out.println ( fourthPowerSum ( n ) );
