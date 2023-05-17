n , var m = map ( int , input ( ) . split ( ) );
var x = min ( n , m );
var li = {};
for i in range ( x + 1 ) :
    var x1 = pow ( i , 2 );
    for j in range ( x + 1 ) :
        var y1 = pow ( j , 2 );
        if (( x1 + j == n and i + y1 == m )) {
            li . append ( ( i , j ) );
        }
 System.out.println ( len ( li ) );
