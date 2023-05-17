import math;
public void countUnsetBits ( n ) {
    var x = n;
    n |= n >> 1;
    n |= n >> 2;
    n |= n >> 4;
    n |= n >> 8;
    n |= n >> 16;
    var t = math . log ( x ^ n , 2 );
    return math . floor ( t );
}
var n = 17;
System.out.println ( countUnsetBits ( n ) );
