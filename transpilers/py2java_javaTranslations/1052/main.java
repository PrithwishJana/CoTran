import math.sqrt;
public void sieve ( prime , n ) {
    prime { 0 } = false ;;
    prime { 1 } = false ;;
    for p in range ( 2 , int ( sqrt ( n ) ) + 1 ) :
        if (( prime { p } == true )) {
            for i in range ( p * p , n + 1 , p ) :
                prime { i } = false ;;
        }
 }
public void sumPrime ( d ) {
    var maxVal = ( 10 ** d ) - 1 ;;
    var prime = { true } * ( maxVal + 1 ) ;;
    sieve ( prime , maxVal ) ;;
    var sum = 0 ;;
    for i in range ( 2 , maxVal + 1 ) :
        if (( prime { i } )) {
            sum += i ;;
        }
     return sum ;;
}
if (var __name__ == "__main__") {
    var d = 3 ;;
    System.out.println ( sumPrime ( d ) ) ;;
}
 