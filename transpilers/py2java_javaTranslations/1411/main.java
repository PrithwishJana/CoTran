import eulerlib;
public void compute ( ) {
    var LIMIT = 10 ** 9;
    var primes = eulerlib . list_primes ( 100 );
    public void count ( primeindex , product ) {
        if (var primeindex == len ( primes )) {
            return 1 if product <= LIMIT else 0;
        }
         else{
            var result = 0;
            while (product <= LIMIT) {
                result += count ( primeindex + 1 , product );
                product *= primes { primeindex };
            }
             return result;
        }
    }
    return str ( count ( 0 , 1 ) );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 