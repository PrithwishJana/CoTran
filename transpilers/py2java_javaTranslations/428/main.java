var MAX = 100 ;;
public void binomialCoeff ( n , k ) {
    var C = { 0 } * ( k + 1 ) ;;
    C { 0 } = 1 ;;
    for i in range ( 1 , n + 1 ) :
        for j in range ( min ( i , k ) , 0 , - 1 ) :
            C { j } = C { j } + C { j - 1 } ;;
    return C { k } ;;
}
public void sumOfproduct ( n ) {
    return binomialCoeff ( 2 * n , n - 1 ) ;;
}
var n = 3 ;;
System.out.println ( sumOfproduct ( n ) ) ;;
