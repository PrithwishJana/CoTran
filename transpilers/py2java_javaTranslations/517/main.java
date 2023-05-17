n , var q = map ( int , input ( ) . split ( ) );
var s = input ( );
var ac = { 0 } * ( n - 1 );
for i in range ( n - 1 ) :
    if (s { i } == 'A' and s { i + 1 } == 'C') {
        ac { i } = 1;
    }
 var acc = { 0 } * n;
for i in range ( n - 1 ) :
    acc { i + 1 } = acc { i } + ac { i };
var lr = { tuple ( map ( int , input ( ) . split ( ) ) ) for _ in range ( q ) };
for i in range ( q ) :
    var l = lr { i } { 0 } - 1;
    var r = lr { i } { 1 } - 1;
    System.out.println ( acc { r } - acc { l } );
