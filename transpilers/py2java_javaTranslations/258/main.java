var MAX = 1000000;
var prime = { true } * ( MAX + 1 );
public void SieveOfEratosthenes ( ) {
    prime { 1 } = false ;;
    prime { 0 } = false ;;
    var p = 2;
    while (p * p <= MAX) {
        if (( prime { p } == true )) {
            for i in range ( p * 2 , MAX + 1 , p ) :
                prime { i } = false;
        }
         p += 1;
    }
 }
public void productOfKthPrimes ( arr , n , k ) {
    var c = 0;
    product = 1;
    for i in range ( n ) :
        if (( prime { arr [ i } ] )) {
            c += 1;
            if (( c % k == 0 )) {
                product *= arr { i };
                c = 0;
            }
         }
     System.out.println ( product );
}
if (var __name__ == "__main__") {
    SieveOfEratosthenes ( );
    var n = 5;
    var k = 2;
    var arr = { 2 , 3 , 5 , 7 , 11 };
    productOfKthPrimes ( arr , n , k );
}
 