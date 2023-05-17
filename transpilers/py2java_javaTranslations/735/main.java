import sys;
import sys.stdin;
var input = stdin . readline;
public void solve ( c , a , n ) {
    CCA , CCC , var CAN = 0 , 0 , 0;
    CAN = min ( c , a , n );
    c -= CAN;
    a -= CAN;
    if (a > 0 and c > 0) {
        var CCA = min ( a , c // 2 );
        c -= ( CCA * 2 );
    }
     if (c > 2) {
        var CCC = c // 3;
    }
     return CAN + CCA + CCC;
}
public void main ( args ) {
    var Q = int ( input ( ) );
    for _ in range ( Q ) :
        c , a , var n = map ( int , input ( ) . split ( ) );
        var ans = solve ( c , a , n );
        System.out.println ( ans );
}
if (var __name__ == '__main__') {
    main ( sys . argv { 1 : } );
}
 