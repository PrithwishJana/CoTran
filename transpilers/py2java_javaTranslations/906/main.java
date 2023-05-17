import math;
public void onesComplement ( n ) {
    var number_of_bits = ( int ) ( math . floor ( math . log ( n ) / math . log ( 2 ) ) ) + 1 ;;
    return ( ( 1 << number_of_bits ) - 1 ) ^ n ;;
}
var n = 22;
System.out.println ( onesComplement ( n ) );
