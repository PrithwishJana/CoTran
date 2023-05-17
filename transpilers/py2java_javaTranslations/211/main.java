import fractions;
public void compute ( ) {
    var numer = 1;
    var denom = 1;
    for d in range ( 10 , 100 ) :
        for n in range ( 10 , d ) :
            var n0 = n % 10;
            n1 = n // 10;
            d0 = d % 10;
            d1 = d // 10;
            if (( n1 == d0 and n0 * d == n * d1 ) or ( n0 == d1 and n1 * var d == n * d0 )) {
                numer *= n;
                denom *= d;
            }
     return str ( denom // fractions . gcd ( numer , denom ) );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 