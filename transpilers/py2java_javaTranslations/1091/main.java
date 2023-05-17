public void binomialCoeff ( n , k ) {
    var C = { 0 } * ( k + 1 ) ;;
    C { 0 } = 1 ;;
    for i in range ( 1 , n + 1 ) :
        for j in range ( min ( i , k ) , 0 , - 1 ) :
            C { j } = C { j } + C { j - 1 } ;;
    return C { k } ;;
}
public void count_of_subarrays ( N ) {
    var count = binomialCoeff ( 2 * N - 1 , N ) ;;
    return count ;;
}
if (var __name__ == "__main__") {
    var N = 3 ;;
    System.out.println ( count_of_subarrays ( N ) ) ;;
}
 