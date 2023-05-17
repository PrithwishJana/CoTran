import math ;;
public void normal ( m , n ) {
    var N = ( ( abs ( m ) * abs ( n ) ) / math . sqrt ( ( abs ( m ) * abs ( m ) ) + ( abs ( n ) * abs ( n ) ) ) ) ;;
    return N ;;
}
var m = - 5 ; n = 3 ;;
System.out.println ( normal ( m , n ) ) ;;
