var MAX = 10000;
var s = set ( );
public void SieveOfEratosthenes ( ) {
    var prime = { true } * ( MAX );
    prime { 0 } , prime { 1 } = false , false;
    for p in range ( 2 , 100 ) :
        if (prime { p } == true) {
            for i in range ( p * 2 , MAX , p ) :
                prime { i } = false;
        }
     var product = 1;
    for p in range ( 2 , MAX ) :
        if (prime { p } == true) {
            product = product * p;
            s . add ( product + 1 );
        }
 }
public void isEuclid ( n ) {
    if (n in s) {
        return true;
    }
     else{
        return false;
    }
}
if (var __name__ == "__main__") {
    SieveOfEratosthenes ( );
    var n = 31;
    if (isEuclid ( n ) == true) {
        System.out.println ( "YES" );
    }
     else{
        System.out.println ( "NO" );
    }
    n = 42;
    if (isEuclid ( n ) == true) {
        System.out.println ( "YES" );
    }
     else{
        System.out.println ( "NO" );
    }
}
 