var n = int ( input ( ) );
var h = ';//'
var f = { [ h } * ( n + 2 ) ];
var a = f + { [ * ( h + input ( ) + h ) } for _ in { 0 } * n ] + f * 2;
for i in range ( n ) :
    for j in range ( n ) :
        if (a { i + 1 } { j + 1 } > h) {
            for k , l in ( 2 , 0 ) , ( 2 , 1 ) , ( 2 , 2 ) , ( 3 , 1 ) :
                if a { i + k } { j + l } == h : System.out.println ( 'NO' ) ; exit ( );
                a { i + k } { j + l } = h;
        }
 System.out.println ( 'YES' );
