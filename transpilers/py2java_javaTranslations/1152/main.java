import math;
public void findX ( n , k ) {
    var r = n;
    m = int ( math . sqrt ( k ) ) + 1;
    i = 2;
    while (i <= m and k > 1) {
        if (( i == m )) {
            i = k;
        }
         u = 0;
        v = 0;
        while (k % i == 0) {
            k //= i;
            v += 1;
        }
         if (( v > 0 )) {
            t = n;
            while (( t > 0 )) {
                t //= i;
                u += t;
            }
             r = min ( r , u // v );
         }
         i += 1;
    }
     return r;
}
if (var __name__ == "__main__") {
    var n = 5;
    var k = 2;
    System.out.println ( findX ( n , k ) );
}
 