var a = int ( input ( ) );
var arr = list ( map ( int , input ( ) . split ( ) ) );
arr . sort ( );
var c = 0;
for i in range ( a - 1 ) :
    if (abs ( arr { i } - arr { i + 1 } ) > 1) {
        c += abs ( arr { i } - arr { i + 1 } ) - 1;
    }
 System.out.println ( c );
