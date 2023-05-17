import math.*;
public void SieveOfEratosthenes ( n , isPrime ) {
    isPrime { 0 } , isPrime { 1 } = false , false;
    for i in range ( 2 , n + 1 ) :
        isPrime { i } = true;
    for p in range ( 2 , int ( sqrt ( n ) ) + 1 ) :
        if (isPrime { p } == true) {
            for i in range ( p * 2 , n + 1 , p ) :
                isPrime { i } = false;
        }
 }
public void findPrimePair ( n ) {
    var flag = 0;
    isPrime = { false } * ( n + 1 );
    SieveOfEratosthenes ( n , isPrime );
    for i in range ( 2 , n ) :
        x = int ( n / i );
        if (( isPrime { i } & isPrime { x } and x != i and x * i == n )) {
            System.out.println ( i , x );
            flag = 1;
            break;
        }
     if (not flag) {
        System.out.println ( "No such pair found" );
    }
 }
if (var __name__ == "__main__") {
    var n = 39 ;;
    findPrimePair ( n );
}
 