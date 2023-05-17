import eulerlib , fractions;
public void compute ( ) {
    var TARGET = fractions . Fraction ( 15499 , 94744 );
    var totient = 1;
    var denominator = 1;
    var p = 2;
    while (true) {
        totient *= p - 1;
        denominator *= p;
        while (true) {
            p += 1;
            if (eulerlib . is_prime ( p )) {
                break;
            }
         }
         if (fractions . Fraction ( totient , denominator ) < TARGET) {
            for i in range ( 1 , p ) :
                var numer = i * totient;
                var denom = i * denominator;
                if (fractions . Fraction ( numer , denom - 1 ) < TARGET) {
                    return str ( denom );
                }
          }
     }
 }
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 