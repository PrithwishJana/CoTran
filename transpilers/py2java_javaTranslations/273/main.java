import sys;
var input = sys . stdin . readline;
n , var m = map ( int , input ( ) . split ( ) );
var w = list ( map ( int , input ( ) . split ( ) ) );
var d = { [ } for i in range ( n ) ];
for i in range ( m ) :
    a , var b = map ( int , input ( ) . split ( ) );
    d { a - 1 } . append ( b );
    d { b - 1 } . append ( a );
var x = {};
for i in range ( n ) :
    if (len ( d { i } ) > 1) {
        for i1 in range ( len ( d { i } ) ) :
            for i2 in range ( i1 + 1 , len ( d { i } ) ) :
                if (( i + 1 in d { d [ i } { i1 } - 1 ] ) and ( d { i } { i2 } in d { d [ i } { i1 } - 1 ] ) and ( i + 1 in d { d [ i } { i2 } - 1 ] ) and ( d { i } { i1 } in d { d [ i } { i2 } - 1 ] )) {
                    var z = ( i + 1 , d { i } { i1 } , d { i } { i2 } );
                    x . append ( z );
                }
     }
 var c1 = 1e9;
for a , b , c in x :
    c1 = min ( c1 , w { a - 1 } + w { b - 1 } + w { c - 1 } );
System.out.println ( c1 if c1 != 1e9 else - 1 );
