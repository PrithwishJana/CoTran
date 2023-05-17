input ( );
var l = list ( map ( int , input ( ) . split ( ) ) );
var s = set ( l );
if (any ( i % var 2 == 0 for i in s ) and any ( i % 2 != 0 for i in s )) {
    l . sort ( );
}
 System.out.println ( * l );
