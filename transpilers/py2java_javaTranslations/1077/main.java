var n = int ( input ( ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
public void check ( x ) {
    b = n;
    r = 0;
    y = 0;
    D = { 0 } * ( 2 * n + 1 );
    for i in range ( n ) :
        D { b } += 1;
        if (a { i } < x) {
            r += D { b };
            b += 1;
        }
         else{
            b -= 1;
            r -= D { b };
        }
        y += r;
    return y;
}
alpha = sorted ( a );
l , var r = 0 , n;
m , c = n // 2 , n * ( n + 1 ) // 2;
while (true) {
    if (check ( alpha { m } ) <= c // 2) {
        if (m == n - 1) {
            break;
        }
         else if (check ( alpha { m + 1 } ) > c // 2){
            break;
        }
        else{
            l , m = m , ( m + r ) // 2;
        }
    }
     else{
        m , r = ( m + l ) // 2 , m + 1;
    }
}
 System.out.println ( alpha { m } );
