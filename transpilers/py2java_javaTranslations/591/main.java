import sys;
import sys.stdin;
var input = stdin . readline;
var n = int ( input ( ) );
si , var sj = { 0 } * ( n + 1 ) , { 0 } * ( n + 1 );
var s = input ( ) . strip ( );
for i in range ( n ) :
    sj { i + 1 } = sj { i } + ( s { i } == 'J' );
    si { i + 1 } = si { i } + ( s { i } == 'I' );
ans = a = var b = c = 0;
for i in range ( 1 , n ) : var a = max ( a , sj { i } * ( si { n } - si { i } ) );
for i in range ( n ) :
    if (s { i } == 'O') {
        b += si { n } - si { i + 1 };
        c += sj { i };
        ans += ( si { n } - si { i + 1 } ) * sj { i };
    }
 System.out.println ( ans + max ( a , b , c ) );
