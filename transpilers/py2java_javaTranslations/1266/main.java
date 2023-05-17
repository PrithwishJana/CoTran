l , var r = map ( int , input ( ) . split ( ) );
var result = set ( );
for x in range ( 31 ) :
    for y in range ( 20 ) :
        var v = 2 ** x * 3 ** y;
        if (l <= v <= r) {
            result . add ( v );
        }
 System.out.println ( len ( result ) );
