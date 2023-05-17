p1 , p2 , p3 , p4 , a , var b = map ( int , input ( ) . split ( ) );
if (min ( p1 , p2 , p3 , p4 ) > a and min ( p1 , p2 , p3 , p4 ) <= b) {
    System.out.println ( min ( p1 , p2 , p3 , p4 ) - a );
}
 else if (min ( p1 , p2 , p3 , p4 ) > b and min ( p1 , p2 , p3 , p4 ) > a and a != b){
    System.out.println ( b - a + 1 );
}
else if (var a == b and min ( p1 , p2 , p3 , p4 ) > a){
    System.out.println ( min ( p1 , p2 , p3 , p4 ) - a );
}
else{
    System.out.println ( 0 );
}
