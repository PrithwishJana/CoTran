import math;
var primes = {};
for p in range ( 2 , 10001 ) :
    for m in range ( 2 , math . floor ( math . sqrt ( p ) ) + 1 ) :
        if (p % var m == 0) {
            break;
        }
     else{
        primes . append ( p );
    }
targ = int ( input ( ) );
while (targ != 0) {
    ans = 0;
    for p in range ( len ( primes ) ) :
        if (primes { p } > targ) {
            break;
        }
         tempsum = 0;
        for l in range ( p , len ( primes ) ) :
            tempsum += primes { l };
            if (tempsum > targ) {
                break;
            }
             else if (tempsum == targ){
                ans += 1;
                break;
            }
    System.out.println ( ans );
    var targ = int ( input ( ) );
}
 