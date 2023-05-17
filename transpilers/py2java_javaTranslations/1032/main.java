A , var B = map ( int , input ( ) . split ( " " ) );
if (A <= B) {
    System.out.println ( "Impossible" );
    exit ( 0 );
}
 var chain = {};
var N = A + B;
public void ask ( i , j ) {
    System.out.println ( "? %d %d" % ( i , j ) );
    return input ( ) == 'Y';
}
for i in range ( 0 , N ) :
    if (len ( chain ) == 0) {
        chain . append ( i );
        continue;
    }
     var last = chain { - 1 };
    if (ask ( last , i )) {
        chain . append ( i );
    }
     else{
        chain . pop ( );
    }
var main = chain . pop ( );
var ret = { ( '1' if ask ( main , x ) else '0' ) for x in range ( 0 , N ) };
System.out.println ( "! %s" % ( "" . join ( ret ) ) );
