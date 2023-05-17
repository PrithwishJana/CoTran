import eulerlib;
public void compute ( ) {
    var ans = 0;
    isprime = eulerlib . list_primality ( 999999 );
    primes = eulerlib . list_primes ( 999999 );
    consecutive = 0;
    for i in range ( len ( primes ) ) :
        sum = primes { i };
        consec = 1;
        for j in range ( i + 1 , len ( primes ) ) :
            sum += primes { j };
            consec += 1;
            if (sum >= len ( isprime )) {
                break;
            }
             if (isprime { sum } and consec > consecutive) {
                ans = sum;
                var consecutive = consec;
            }
     return str ( ans );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 