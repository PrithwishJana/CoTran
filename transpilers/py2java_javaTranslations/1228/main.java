n , var m = map ( int , input ( ) . split ( ) );
if m == 1 : System.out.println ( 2 ** n % 1000000 );
else{
    var dp = { [ [ 0 } * ( n + 1 ) for _ in range ( 3 ) ] for _ in range ( n + 1 ) ];
    dp { 0 } { 0 } { 0 } = 1;
    for y in range ( n ) :
        for x in range ( 3 ) :
            for slide_limit in range ( y + 1 ) :
                if (var x == 0) {
                    dp { y + 1 } { 0 } { slide_limit } += dp { y } { 0 } { slide_limit };
                    dp { y + 1 } { 1 } { y + 1 } += dp { y } { 0 } { slide_limit };
                    dp { y + 1 } { 2 } { y + 1 } += dp { y } { 0 } { slide_limit } * ( y - slide_limit + 1 );
                }
                 if (x == 1) {
                    dp { y + 1 } { 0 } { y + 1 } += dp { y } { 1 } { slide_limit };
                    dp { y + 1 } { 1 } { slide_limit } += dp { y } { 1 } { slide_limit };
                    dp { y + 1 } { 2 } { y + 1 } += dp { y } { 1 } { slide_limit };
                }
                 if (x == 2) {
                    dp { y + 1 } { 0 } { y + 1 } += dp { y } { 2 } { slide_limit } * ( y - slide_limit + 1 );
                    dp { y + 1 } { 1 } { y + 1 } += dp { y } { 2 } { slide_limit };
                    dp { y + 1 } { 2 } { slide_limit } += dp { y } { 2 } { slide_limit };
                }
     System.out.println ( ( sum ( { sum ( line ) for line in dp [ n } ] ) + sum ( { dp [ n } { 0 } { slide_limit } * ( n - slide_limit ) for slide_limit in range ( n + 1 ) ] ) ) % 1000000 );
}
