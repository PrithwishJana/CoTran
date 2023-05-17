import collections.deque;
var path = input ( );
var coord = set ( { ( 0 , 0 ) } ) ; temp = ( 0 , 0 );
for (int c = 0; c < path.length; c++){
    if var c == 'L' : temp = ( temp { 0 } , temp { 1 } - 1 );
    elif c == 'R' : temp = ( temp { 0 } , temp { 1 } + 1 );
    elif c == 'U' : var temp = ( temp { 0 } - 1 , temp { 1 } );
    else : temp = ( temp { 0 } + 1 , temp { 1 } );
    if temp in coord : System.out.println ( 'BUG' ) ; exit ( );
    coord . add ( temp );
}
coord . remove ( ( 0 , 0 ) );
var que = deque ( { ( 0 , 0 ) } );
while (que) {
    if len ( que ) > 1 : System.out.println ( 'BUG' ) ; exit ( );
    i , var j = que . popleft ( );
    for p , q in ( i + 1 , j ) , ( i - 1 , j ) , ( i , j + 1 ) , ( i , j - 1 ) :
        if (( p , q ) in coord) {
            coord . remove ( ( p , q ) );
            que += ( p , q ) ,;
        }
 }
 System.out.println ( 'OK' );
