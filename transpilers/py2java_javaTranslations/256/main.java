var MAX = 100000 ;;
var prime = { true } * ( MAX + 1 ) ;;
public void SieveOfEratosthenes ( ) {
    prime { 1 } = false ;;
    prime { 0 } = false ;;
    var p = 2 ;;
    while (( p * p <= MAX )) {
        if (( prime { p } )) {
            var i = p * 2 ;;
            while (( i <= MAX )) {
                prime { i } = false ;;
                i += p ;;
            }
        }
          p += 1 ;;
    }
 }
public void SumOfKthPrimes ( arr , n , k ) {
    var c = 0 ;;
    sum = 0 ;;
    for i in range ( n ) :
        if (( prime { arr [ i } ] )) {
            c += 1 ;;
            if (( c % k == 0 )) {
                sum += arr { i } ;;
                c = 0 ;;
            }
         }
     System.out.println ( sum ) ;;
}
SieveOfEratosthenes ( ) ;;
var arr = { 2 , 3 , 5 , 7 , 11 } ;;
var n = len ( arr ) ;;
var k = 2 ;;
SumOfKthPrimes ( arr , n , k ) ;;
