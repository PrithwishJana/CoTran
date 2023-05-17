var MAX = 10000;
var arr = {};
public void SieveOfEratosthenes ( ) {
    var prime = { true } * MAX;
    var p = 2;
    while (p * p < MAX) {
        if (( prime { p } == true )) {
            for i in range ( p * 2 , MAX , p ) :
                prime { i } = false;
        }
         p += 1;
    }
     for p in range ( 2 , MAX ) :
        if (( prime { p } )) {
            arr . append ( p );
        }
 }
public void isEuclid ( n ) {
    var product = 1;
    i = 0;
    while (( product < n )) {
        product = product * arr { i };
        if (( product + var 1 == n )) {
            return true;
        }
         i += 1;
    }
     return false;
}
if (var __name__ == "__main__") {
    SieveOfEratosthenes ( );
    var n = 31;
    if (( isEuclid ( n ) )) {
        System.out.println ( "YES" );
    }
     else{
        System.out.println ( "NO" );
    }
    n = 42;
    if (( isEuclid ( n ) )) {
        System.out.println ( "YES" );
    }
     else{
        System.out.println ( "NO" );
    }
}
 