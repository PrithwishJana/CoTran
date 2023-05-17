import math.sqrt;
var MAX = 100000;
var prime = { true } * ( MAX + 1 );
public void SieveOfEratosthenes ( ) {
    for p in range ( 2 , int ( sqrt ( MAX ) ) + 1 ) :
        if (( prime { p } == true )) {
            for i in range ( p * p , MAX + 1 , p ) :
                prime { i } = false ;;
        }
 }
public void smallestPrime ( d ) {
    var l = 10 ** ( d - 1 ) ;;
    r = ( 10 ** d ) - 1 ;;
    for i in range ( l , r + 1 ) :
        if (( prime { i } )) {
            return i ;;
        }
     return - 1 ;;
}
public void largestPrime ( d ) {
    l = 10 ** ( d - 1 ) ;;
    var r = ( 10 ** d ) - 1 ;;
    for i in range ( r , l , - 1 ) :
        if (( prime { i } )) {
            return i ;;
        }
     return - 1 ;;
}
if (var __name__ == "__main__") {
    SieveOfEratosthenes ( ) ;;
    var queries = { 2 , 5 } ;;
    var q = len ( queries ) ;;
    for i in range ( q ) :
        System.out.println ( smallestPrime ( queries { i } ) , largestPrime ( queries { i } ) ) ;;
}
 