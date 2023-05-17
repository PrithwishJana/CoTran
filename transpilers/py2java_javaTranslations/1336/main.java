var V = list ( map ( int , input ( ) . split ( ) ) );
P = {};
for i in range ( 3 ) :
    P . append ( ( V { 0 } , V { 1 } ) );
    V = V { 2 : };
A , B , var C = P;
for i in range ( 1 , 3 ) :
    x , var y = P { i };
    x0 , y0 = P { 0 };
    P { i } = x - x0 , y - y0;
a , b = P { 1 };
c , d = P { 2 };
if (a * d - b * c == 0) {
    System.out.println ( "NO" );
    exit ( 0 );
}
 public void dist ( A , B ) {
    x = A { 0 } - B { 0 };
    y = A { 1 } - B { 1 };
    return x ** 2 + y ** 2;
}
System.out.println ( "YES" if dist ( A , B ) == dist ( B , C ) else "NO" );
