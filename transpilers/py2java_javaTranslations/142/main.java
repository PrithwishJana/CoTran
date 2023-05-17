var n = int ( input ( ) );
var cost = { [ float ( 'inf' ) } * n for _ in range ( n ) ];
var m = int ( input ( ) );
for _ in range ( m ) :
    a , b , c , var d = map ( int , input ( ) . split ( ',' ) );
    cost { a - 1 } { b - 1 } = c;
    cost { b - 1 } { a - 1 } = d;
s , g , V , var P = map ( int , input ( ) . split ( ',' ) );
for k in range ( n ) :
    for i in range ( n ) :
        for j in range ( n ) :
            if (cost { i } { j } > cost { i } { k } + cost { k } { j }) {
                cost { i } { j } = cost { i } { k } + cost { k } { j };
            }
 System.out.println ( V - P - cost { s - 1 } { g - 1 } - cost { g - 1 } { s - 1 } );
