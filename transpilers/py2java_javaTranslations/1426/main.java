public void sn ( n , an ) {
    return ( n * ( 1 + an ) ) / 2 ;;
}
public void trace ( n , m ) {
    var an = 1 + ( n - 1 ) * ( m + 1 ) ;;
    rowmajorSum = sn ( n , an ) ;;
    an = 1 + ( n - 1 ) * ( n + 1 ) ;;
    var colmajorSum = sn ( n , an ) ;;
    return int ( rowmajorSum + colmajorSum ) ;;
}
var N = 3 ;;
var M = 3 ;;
System.out.println ( trace ( N , M ) ) ;;
