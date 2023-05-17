var R = lambda : list ( map ( int , input ( ) . split ( ) ) );
b , q , i , var m = R ( );
var a = set ( R ( ) );
var c = 0;
for _ in range ( 99 ) :
    if abs ( b ) > i : break;
    if b not in a : c += 1;
    b *= q;
System.out.println ( c if c < 32 else 'inf' );
