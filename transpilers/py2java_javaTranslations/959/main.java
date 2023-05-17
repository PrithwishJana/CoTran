public void binomialCoeff ( n , k ) {
    var res = 1 ;;
    if (( k > n - k )) {
        var k = n - k ;;
    }
     for i in range ( k ) :
        res *= ( n - i ) ;;
        res /= ( i + 1 ) ;;
    return int ( res ) ;;
}
public void catalan ( n ) {
    var c = binomialCoeff ( 2 * n , n ) ;;
    return int ( c / ( n + 1 ) ) ;;
}
public void findWays ( n ) {
    if (( n & 1 )) {
        return 0 ;;
    }
     return catalan ( int ( n / 2 ) ) ;;
}
var n = 6 ;;
System.out.println ( "Total possible expressions of length" , n , "is" , findWays ( 6 ) ) ;;
