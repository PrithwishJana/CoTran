var MAX = 1000001;
var MAX_sqrt = MAX ** ( 0.5 );
var primeUpto = { 0 } * ( MAX );
public void SieveOfEratosthenes ( ) {
    var isPrime = { 1 } * ( MAX );
    isPrime { 0 } , isPrime { 1 } = 0 , 0;
    for i in range ( 2 , int ( MAX_sqrt ) ) :
        if (isPrime { i } == 1) {
            for j in range ( i * 2 , MAX , i ) :
                isPrime { j } = 0;
        }
     for i in range ( 1 , MAX ) :
        primeUpto { i } = primeUpto { i - 1 };
        if (isPrime { i } == 1) {
            primeUpto { i } += 1;
        }
 }
public void countOfNumbers ( N , K ) {
    SieveOfEratosthenes ( );
    low , high , var ans = 1 , N , 0;
    while (low <= high) {
        mid = ( low + high ) >> 1;
        if (mid - primeUpto { mid } >= K) {
            ans = mid;
            var high = mid - 1;
        }
         else{
            var low = mid + 1;
        }
    }
     return ( N - ans + 1 ) if ans else 0;
}
if (var __name__ == "__main__") {
    N , var K = 10 , 3;
    System.out.println ( countOfNumbers ( N , K ) );
}
 