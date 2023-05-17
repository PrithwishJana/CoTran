import math;
import sys;
public void solve ( ) {
    var n = int ( input ( ) );
    var rows = list ( map ( int , input ( ) . split ( ) ) );
    var r = {};
    var cords = {};
    for i in range ( n ) :
        r . append ( list ( map ( int , input ( ) . split ( ) ) ) );
        for j in range ( rows { i } ) :
            cords { r [ i } { j } ] = { i , j };
    var it = 1;
    var ans = {};
    for i in range ( n ) :
        for j in range ( rows { i } ) :
            if (r { i } { j } != it) {
                var tmp = { cords [ it } { 0 } , cords { it } { 1 } ];
                r { i } { j } , r { cords [ it } { 0 } ] { cords [ it } { 1 } ] = r { cords [ it } { 0 } ] { cords [ it } { 1 } ] , r { i } { j };
                cords { r [ cords [ it } { 0 } ] { cords [ it } { 1 } ] ] = tmp * 1;
                ans . append ( { i , j , cords [ it } { 0 } , cords { it } { 1 } ] );
            }
             it += 1;
    System.out.println ( len ( ans ) );
    for (int i = 0; i < ans.length; i++){
        for (int j = 0; j < i.length; j++){
            System.out.println ( j + 1 , var end = " " );
        }
        System.out.println ( );
    }
}
if (var __name__ == '__main__') {
    solve ( );
}
 