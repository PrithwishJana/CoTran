import io , os , sys;
import collections.Counter;
var t = int ( input ( ) );
public void GO_LIFE ( ) {
    var a = list ( input ( ) );
    var b = list ( input ( ) );
    var p = Counter ( a );
    var n = len ( a );
    var ok = 0;
    for (int i = 0; i < b.length; i++){
        if (p { i } == 0) {
            ok = 1;
        }
    }
     if (b != sorted ( b ) or ok == 1) {
        for i in sorted ( a ) :
            System.out.println ( i , var end = "" );
        System.out.println ( );
        return;
    }
     a . sort ( );
    q1 = {};
    q2 = {};
    q = {};
    for i in range ( n - 1 , - 1 , - 1 ) :
        if (a { i } == 'c') {
            q += { i };
        }
         if (a { i } == 'b') {
            q1 . insert ( 0 , i );
        }
     i , j = 0 , 0;
    while (j < len ( q1 ) and i < len ( q )) {
        a { q [ i } ] , a { q1 [ j } ] = a { q1 [ j } ] , a { q [ i } ];
        i += 1;
        j += 1;
    }
     for (int i = 0; i < a.length; i++){
        System.out.println ( i , end = "" );
     }
    System.out.println ( );
}
while (t > 0) {
    GO_LIFE ( );
    t -= 1;
}
 