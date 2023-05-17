import math;
public void nthElement ( a , b , n ) {
    var lcm = ( a * b ) / int ( math . gcd ( a , b ) );
    var l = 1;
    r = min ( a , b ) * n;
    while (( l <= r )) {
        mid = ( l + r ) >> 1;
        val = ( int ( mid / a ) + int ( mid / b ) - int ( mid / lcm ) );
        if (( val == n )) {
            return int ( max ( int ( mid / a ) * a , int ( mid / b ) * b ) );
        }
         if (( val < n )) {
            l = mid + 1;
        }
         else{
            var r = mid - 1;
        }
    }
 }
var a = 5;
var b = 3;
var n = 5;
System.out.println ( nthElement ( a , b , n ) );
