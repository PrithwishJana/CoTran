import math;
public void isPower ( n ) {
    if (( var n == 1 )) {
        return true;
    }
     for x in range ( 2 , ( int ) ( math . sqrt ( n ) ) + 1 ) :
        var y = 2;
        p = ( int ) ( math . pow ( x , y ) );
        while (( p <= n and p > 0 )) {
            if (( p == n )) {
                return true;
            }
             y = y + 1;
            var p = math . pow ( x , y );
        }
     return false;
}
for i in range ( 2 , 100 ) :
    if (( isPower ( i ) )) {
        System.out.println ( i , var end = " " );
    }
 