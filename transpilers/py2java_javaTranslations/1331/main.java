var t = int ( input ( ) );
var i = 1;
while (true) {
    if (i > t) {
        break;
    }
     n , a , b , c , d = map ( int , input ( ) . split ( ) );
    if (n * ( a - b ) > ( c + d ) or n * ( a + b ) < ( c - d )) {
        System.out.println ( "No" );
    }
     else{
        System.out.println ( "Yes" );
    }
    i = i + 1;
}
 