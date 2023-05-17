import eulerlib;
public void compute ( ) {
    var LIMIT = 50000000;
    var primes = eulerlib . list_primes ( eulerlib . sqrt ( LIMIT ) );
    var sums = { 0 };
    for i in range ( 2 , 5 ) :
        newsums = set ( );
        for (int p = 0; p < primes.length; p++){
            q = p ** i;
            if (q > LIMIT) {
                break;
            }
             for (int x = 0; x < sums.length; x++){
                if (x + q <= LIMIT) {
                    newsums . add ( x + q );
                }
             }
        }
         sums = newsums;
    return str ( len ( sums ) );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 