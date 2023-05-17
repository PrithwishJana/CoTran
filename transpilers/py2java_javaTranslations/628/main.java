import math;
public void isPower ( n ) {
    if (( n <= 1 )) {
        return true;
    }
     for x in range ( 2 , ( int ) ( math . sqrt ( n ) ) + 1 ) :
        var p = x;
        while (( p <= n )) {
            p = p * x;
            if (( p == n )) {
                return true;
            }
         }
     return false;
}
for i in range ( 2 , 100 ) :
    if (( isPower ( i ) )) {
        System.out.println ( i , var end = " " );
    }
 