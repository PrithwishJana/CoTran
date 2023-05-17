public void ProdOfPrimes ( n ) {
    var prime = { true for i in range ( n + 1 ) };
    var p = 2;
    while (( p * p <= n )) {
        if (( prime { p } == true )) {
            var i = p * 2;
            while (( i <= n )) {
                prime { i } = false;
                i += p;
            }
        }
          p += 1;
    }
     var prod = 1;
    for i in range ( 2 , n + 1 ) :
        if (( prime { i } )) {
            prod *= i;
        }
     return prod;
}
var n = 10;
System.out.println ( ProdOfPrimes ( n ) );
