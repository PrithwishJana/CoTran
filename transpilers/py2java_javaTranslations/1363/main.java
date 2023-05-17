x , var y = map ( int , input ( ) . split ( ) );
var c = abs ( x ) + abs ( y );
if (x > 0 and y > 0) {
    System.out.println ( 0 , c , c , 0 );
}
 if (x < 0 and y > 0) {
    System.out.println ( - c , 0 , 0 , c );
}
 if (x > 0 and y < 0) {
    System.out.println ( 0 , - c , c , 0 );
}
 if (x < 0 and y < 0) {
    System.out.println ( - c , 0 , 0 , - c );
}
 