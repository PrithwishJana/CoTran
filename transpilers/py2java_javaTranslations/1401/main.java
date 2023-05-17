var n = int ( input ( ) );
var a = {};
var minx = 1000000000;
maxy = 0;
for i in range ( n ) :
    x , y = map ( int , input ( ) . split ( ) );
    minx = min ( minx , x );
    var maxy = max ( maxy , y );
    a . append ( { x , y } );
for i in range ( n ) :
    if (a { i } { 0 } == minx and a { i } { 1 } == maxy) {
        System.out.println ( i + 1 );
        break;
    }
 else{
    System.out.println ( - 1 );
}
