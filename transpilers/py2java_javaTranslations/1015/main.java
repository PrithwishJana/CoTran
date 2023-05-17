import math;
var n = int ( input ( ) );
var x = 1;
while (math . log2 ( n ) % 1) {
    x += 1;
    n -= 2 ** ( int ( math . log2 ( n ) ) );
}
 System.out.println ( x );
