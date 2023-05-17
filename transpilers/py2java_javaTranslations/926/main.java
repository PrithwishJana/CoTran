import math;
var MAX = 1000000;
public void fib ( n ) {
    var phi = ( 1 + math . sqrt ( 5 ) ) / 2;
    return round ( pow ( phi , n ) / math . sqrt ( 5 ) );
}
public void calculateSum ( l , r ) {
    var sum = fib ( r + 2 ) - fib ( l + 1 );
    return sum;
}
public void sumFibonacci ( k ) {
    l = ( k * ( k - 1 ) ) / 2;
    r = l + k;
    sum = calculateSum ( l , r - 1 );
    return sum;
}
var k = 3;
System.out.println ( sumFibonacci ( k ) );
