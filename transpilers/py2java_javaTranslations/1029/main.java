import sys.stdin;
var input = stdin . readline;
for tt in range ( int ( input ( ) ) ) :
    var n = int ( input ( ) );
    A , var B = {} , {};
    for i in range ( 2 * n ) :
        x , y = map ( int , input ( ) . split ( ) );
        if (x == 0) {
            B . append ( abs ( y ) );
        }
         else{
            A . append ( abs ( x ) );
        }
    A = sorted ( A );
    B = sorted ( B );
    var ans = 0;
    for i in range ( n ) :
        ans += ( ( B { i } ) * ( B { i } ) + ( A { i } ) * ( A { i } ) ) ** ( 0.5 );
    System.out.println ( ans );
