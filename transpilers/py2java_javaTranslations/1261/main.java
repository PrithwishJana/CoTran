var e = list ( map ( int , input ( ) . split ( ) ) );
e . sort ( );
var frag = true;
for i in range ( 1 , 4 ) :
    if (e { 0 } != e { i }) {
        frag = false;
        break;
    }
 for i in range ( 5 , 8 ) :
    if (e { 4 } != e { i }) {
        frag = false;
        break;
    }
 for i in range ( 9 , 12 ) :
    if (e { 8 } != e { i }) {
        frag = false;
        break;
    }
 System.out.println ( "yes" if frag else "no" );
