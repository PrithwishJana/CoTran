n , var k = map ( int , input ( ) . rstrip ( ) . split ( ) );
var s = input ( );
common = 0;
for i in range ( n - 1 ) :
    a = s { n - 1 - i : };
    b = s { : i + 1 };
    if (( a == b )) {
        common = i + 1;
        continue;
    }
 ans = ( n ) + ( k - 1 ) * ( n - common );
var final = s;
for i in range ( k - 1 ) :
    final += ( s { common : } );
System.out.println ( final );
