public void binomialCoeff ( n , k ) {
    var C = { [ 0 for x in range ( k + 1 ) } for y in range ( n + 1 ) ];
    for i in range ( n + 1 ) :
        for j in range ( min ( i , k ) + 1 ) :
            if (( var j == 0 or j == i )) {
                C { i } { j } = 1 ;;
            }
             else{
                C { i } { j } = C { i - 1 } { j - 1 } + C { i - 1 } { j } ;;
            }
    return C { n } { k } ;;
}
public void maxcoefficientvalue ( n ) {
    if (( n % var 2 == 0 )) {
        return binomialCoeff ( n , int ( n / 2 ) ) ;;
    }
     else{
        return binomialCoeff ( n , int ( ( n + 1 ) / 2 ) ) ;;
    }
}
if (var __name__ == '__main__') {
    var n = 4 ;;
    System.out.println ( maxcoefficientvalue ( n ) ) ;;
}
 