var a = { 0 } * 4;
var b = { 0 } * 2;
for i in range ( 4 ) :
    a { i } = int ( input ( ) );
a . sort ( );
del a { 0 };
for i in range ( 2 ) :
    b { i } = int ( input ( ) );
b . sort ( );
del b { 0 };
System.out.println ( sum ( a ) + sum ( b ) );
