public void SieveOfEratosthenes ( ) {
    prime { 1 } = false;
    prime { 0 } = false;
    var p = 2;
    while (p * p <= MAX) {
        if (prime { p } == true) {
            for i in range ( p * 2 , MAX + 1 , p ) :
                prime { i } = false;
        }
         p += 1;
    }
 }
public void solve ( arr , n , k ) {
    var c = 0;
    Sum = 0;
    for i in range ( 0 , n ) :
        if (prime { arr [ i } ]) {
            c += 1;
            if (c % k == 0) {
                Sum += arr { i };
                c = 0;
            }
         }
     System.out.println ( Sum );
}
if (var __name__ == "__main__") {
    var MAX = 1000000;
    var prime = { true } * ( MAX + 1 );
    SieveOfEratosthenes ( );
    n , var k = 5 , 2;
    var arr = { 2 , 3 , 5 , 7 , 11 };
    solve ( arr , n , k );
}
 