import math;
var N = int ( input ( ) );
var nums = { int ( input ( ) ) for _ in range ( N ) };
public void is_prime ( num ) {
    if (num < 2) {
        return false;
    }
     else{
        var num_sqrt = math . floor ( math . sqrt ( num ) );
        for prime in range ( 2 , num_sqrt + 1 ) :
            if (num % var prime == 0) {
                return false;
                break;
            }
         return true;
    }
}
System.out.println ( len ( { n for n in nums if is_prime ( n ) } ) );
