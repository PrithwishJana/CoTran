public void sieveOfEratosthenes ( N , s ) {
    var prime = { false } * ( N + 1 );
    for i in range ( 2 , N + 1 , 2 ) :
        s { i } = 2;
    for i in range ( 3 , N + 1 , 2 ) :
        if (( prime { i } == false )) {
            s { i } = i;
            for j in range ( i , int ( N / i ) + 1 , 2 ) :
                if (( prime { i * j } == false )) {
                    prime { i * j } = true;
                    s { i * j } = i;
                }
         }
 }
public void generatePrimeFactors ( N ) {
    var s = { 0 } * ( N + 1 );
    sieveOfEratosthenes ( N , s );
    System.out.println ( "Factor Power" );
    var curr = s { N };
    cnt = 1;
    while (( N > 1 )) {
        N //= s { N };
        if (( curr == s { N } )) {
            cnt += 1;
            continue;
        }
         System.out.println ( str ( curr ) + "\t" + str ( cnt ) );
        curr = s { N };
        var cnt = 1;
    }
 }
var N = 360;
generatePrimeFactors ( N );
