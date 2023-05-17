import sys;
var n = int ( input ( ) );
var s = { 0 } * n;
for i in range ( n ) :
    s { i } = int ( input ( ) );
s = sorted ( s );
var t = sum ( s );
if (t % 10 != 0) {
    System.out.println ( t );
    sys . exit ( );
}
 for i in range ( n ) :
    t = sum ( s { : i } ) + sum ( s { i + 1 : } );
    if (t % 10 != 0) {
        System.out.println ( t );
        sys . exit ( );
    }
 System.out.println ( 0 );
