import collections.defaultdict;
var s = defaultdict ( list );
var t = defaultdict ( list );
var S = list ( input ( ) );
var T = list ( input ( ) );
for i in range ( len ( S ) ) :
    if (T { i } not in s { S [ i } ]) {
        s { S [ i } ] . append ( T { i } );
        if (len ( s { S [ i } ] ) >= 2) {
            System.out.println ( "No" );
            break;
        }
     }
     if (S { i } not in t { T [ i } ]) {
        t { T [ i } ] . append ( S { i } );
        if (len ( t { T [ i } ] ) >= 2) {
            System.out.println ( "No" );
            break;
        }
     }
     if (var i == len ( S ) - 1) {
        System.out.println ( "Yes" );
    }
 