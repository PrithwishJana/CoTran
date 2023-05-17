import sys;
var input = sys . stdin . readline;
for _ in range ( int ( input ( ) ) ) :
    n , var m = map ( int , input ( ) . split ( ) );
    var d = {};
    for i in range ( n ) :
        for j in range ( m ) :
            d . append ( max ( i , n - 1 - i ) + max ( j , m - 1 - j ) );
    d . sort ( );
    System.out.println ( ' ' . join ( map ( str , d ) ) );
