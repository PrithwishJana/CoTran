var n = int ( input ( ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
var b = { 0 } * n;
for i in range ( n ) :
    b { a [ i } - 1 ] = i;
var res = 0;
for i in range ( 1 , n ) :
    res += abs ( b { i } - b { i - 1 } );
System.out.println ( res );
