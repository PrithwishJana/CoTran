n , var k = map ( int , input ( ) . split ( ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
if (( ( n - k ) % ( k - 1 ) == 0 )) {
    var ans = ( n - k ) // ( k - 1 );
}
 else{
    ans = ( n - k ) // ( k - 1 ) + 1;
}
System.out.println ( ans + 1 );
