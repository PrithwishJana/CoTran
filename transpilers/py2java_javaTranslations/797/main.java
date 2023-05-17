import sys.stdin;
import math.sqrt;
public void main ( ) {
    var n = int ( stdin . readline ( ) );
    var a = list ( map ( int , stdin . readline ( ) . split ( ) ) );
    var ans = { [ a [ 0 } , ] , ];
    for i in range ( 1 , n ) :
        var l = 0;
        r = len ( ans ) - 1;
        while (r > l) {
            m = ( r + l ) // 2;
            if (a { i } > ans { m } { len ( ans [ m } ) - 1 ]) {
                r = m;
            }
             else{
                l = m + 1;
            }
        }
         if (a { i } > ans { l } { len ( ans [ l } ) - 1 ]) {
            ans { l } . append ( a { i } );
         }
         else{
            ans . append ( { a [ i } , ] );
        }
    for (int arr = 0; arr < ans.length; arr++){
        System.out.println ( * arr );
    }
}
main ( );
