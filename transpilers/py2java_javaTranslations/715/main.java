import itertools;
while (true) {
    n , var x = map ( int , input ( ) . split ( ' ' ) );
    if ( n == 0 ) & ( x == 0 ) : break;
    var ret = 0;
    for v in itertools . combinations ( list ( range ( 1 , n + 1 ) ) , 3 ) :
        if (sum ( v ) == x) {
            ret += 1;
        }
     System.out.println ( ret );
}
 