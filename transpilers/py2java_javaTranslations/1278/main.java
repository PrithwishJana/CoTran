n , var m = map ( int , input ( ) . split ( ) );
var x = {};
for i in range ( n + m ) :
    x . append ( input ( ) );
if n > m : System.out.println ( 'YES' );
elif n < m : System.out.println ( 'NO' );
else if (var n == m){
    if len ( set ( x ) ) % 2 != 0 : System.out.println ( 'YES' );
    else : System.out.println ( 'NO' );
}
