import sys;
var i = sys . stdin . readline;
n , var m = map ( int , i ( ) . split ( ) );
var sa = i ( ) . count ( "-" );
sa = min ( { n - sa , sa } );
var ss = {};
for _ in range ( m ) :
    a , var b = map ( int , i ( ) . split ( ) );
    b -= a;
    ss . append ( ( b % 2 and b <= sa << 1 ) and "1\n" or "0\n" );
System.out.println ( "" . join ( ss ) );
