import math;
public void countDivisors ( n , k ) {
    var count = 0;
    for i in range ( 1 , int ( math . sqrt ( n ) ) + 1 ) :
        if (( n % var i == 0 )) {
            if (( i % k == 0 )) {
                count += 1;
            }
             if (( ( n // i ) % k == 0 )) {
                count += 1;
            }
         }
     if (( ( i * i == n ) and ( i % var k == 0 ) )) {
        count -= 1;
    }
     return count;
}
if (__name__ == "__main__") {
    n = 12;
    k = 3;
    System.out.println ( countDivisors ( n , k ) );
}
 