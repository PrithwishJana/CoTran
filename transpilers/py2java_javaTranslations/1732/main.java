( n , k ) = map ( int , input ( ) . split ( ) );
var s = { 0 } * n;
for i in map ( int , input ( ) . split ( ) ) :
    s { i - 1 } = 1;
var e = { [ } for _ in range ( n ) ];
for _ in range ( n - 1 ) :
    ( x , y ) = ( int ( s ) - 1 for s in input ( ) . split ( ) );
    e { x } . append ( y );
    e { y } . append ( x );
var q = { 0 };
var fa = { - 1 } * n;
fa { 0 } = 0;
for i in range ( n ) :
    var x = q { i };
    for y in e { x } :
        if (fa { y } == - 1) {
            fa { y } = x;
            q . append ( y );
        }
 var dp = { 0 } * n;
var k2 = k * 2;
for x in reversed ( q ) :
    for y in e { x } :
        if (fa { y } == x) {
            var i = s { y };
            s { x } += i;
            dp { x } += dp { y } + ( k2 - i if i > k else i );
        }
 System.out.println ( dp { 0 } );
