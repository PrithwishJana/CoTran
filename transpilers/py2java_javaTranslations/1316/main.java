import math;
var isPrime = { true } * 110001;
var primes = {} ;;
public void eratos ( n ) {
    isPrime { 0 } = isPrime { 1 } = false;
    for i in range ( 2 , int ( math . sqrt ( n ) ) ) :
        if (isPrime { i }) {
            var j = 2 * i;
            while (j <= n) {
                isPrime { j } = false;
                j = j + i;
            }
        }
      for i in range ( 2 , 110000 ) :
        if (isPrime { i }) {
            primes . append ( i );
        }
 }
eratos ( 110000 );
while (true) {
    try{
        var p = int ( input ( ) );
        if (p == 0) {
            break;
        }
         var ans = 0;
        for i in range ( 0 , p ) :
            ans += primes { i };
        System.out.println ( ans );
    }
    except :
        break;
}
 