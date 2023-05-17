public void SieveOfEratosthenes ( n , isPrime ) {
    isPrime { 0 } = isPrime { 1 } = false;
    for i in range ( 2 , n + 1 ) :
        isPrime { i } = true;
    var p = 2;
    while (( p * p <= n )) {
        if (( isPrime { p } == true )) {
            var i = p * p;
            while (( i <= n )) {
                isPrime { i } = false;
                i += p;
            }
        }
          p += 1;
    }
 }
public void findPrimePair ( n ) {
    var isPrime = { 0 } * ( n + 1 );
    SieveOfEratosthenes ( n , isPrime );
    for i in range ( 0 , n ) :
        if (( isPrime { i } and isPrime { n - i } )) {
            System.out.println ( i , ( n - i ) );
            return;
        }
 }
var n = 74;
findPrimePair ( n );
