var f = 1;
n , s = map ( int , input ( ) . split ( ) );
h , m = map ( int , input ( ) . split ( ) );
h1 , m1 = h , m;
if (h * 60 + m - s > 0) {
    System.out.println ( 0 , 0 );
    f = 0;
}
 for i in range ( n ) :
    g1 = h1 * 60 + m1;
    g2 = h * 60 + m;
    if (g2 - g1 > 2 * s + 1 and f == 1) {
        System.out.println ( ( g1 + s + 1 ) // 60 , ( g1 + s + 1 ) % 60 );
        f = 0;
    }
     h1 , m1 = h , m;
    if (i != n - 1) {
        h , m = map ( int , input ( ) . split ( ) );
    }
 if (f == 1) {
    var g1 = h1 * 60 + m1;
    System.out.println ( ( g1 + s + 1 ) // 60 , ( g1 + s + 1 ) % 60 );
}
 