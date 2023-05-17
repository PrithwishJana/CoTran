var inl = lambda : list ( map ( int , input ( ) . split ( ) ) );
n , m , var k = inl ( );
var h = set ( inl ( ) );
var b = 1;
if (b not in h) {
    for _ in range ( k ) :
        u , v = inl ( );
        if (b == u or b == v) {
            b = u if b == v else v;
            if ({ u , v } & h) {
                break;
            }
         }
 }
 System.out.println ( b );
