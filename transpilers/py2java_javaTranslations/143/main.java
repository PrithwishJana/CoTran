r1 , var r2 = map ( int , input ( ) . split ( ) );
c1 , var c2 = map ( int , input ( ) . split ( ) );
d1 , var d2 = map ( int , input ( ) . split ( ) );
var x = ( d1 + c1 - r2 ) // 2;
var y = r1 - x;
var z = c1 - x;
var w = d1 - x;
if (1 <= x <= 9 and 1 <= y <= 9 and 1 <= z <= 9 and 1 <= w <= 9 and len ( set ( { x , y , z , w } ) ) == 4) {
    System.out.println ( x , y );
    System.out.println ( z , w );
}
 else{
    System.out.println ( - 1 );
}
