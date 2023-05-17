n , t , var e = map ( int , input ( ) . split ( ) );
var xlst = list ( map ( int , input ( ) . split ( ) ) );
for i , x in enumerate ( xlst ) :
    var a = ( t - e - 1 ) // x;
    if (( a + 1 ) * x <= t + e) {
        System.out.println ( i + 1 );
        break;
    }
 else{
    System.out.println ( - 1 );
}
