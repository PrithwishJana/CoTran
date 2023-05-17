public void y ( x ) {
    return ( 1 / ( 1 + x ) );
}
public void BooleRule ( a , b ) {
    var n = 4;
    var h = ( ( b - a ) / n );
    var sum = 0;
    bl = ( 7 * y ( a ) + 32 * y ( a + h ) + 12 * y ( a + 2 * h ) + 32 * y ( a + 3 * h ) + 7 * y ( a + 4 * h ) ) * 2 * h / 45;
    sum = sum + bl;
    return sum;
}
if (var __name__ == '__main__') {
    var lowlimit = 0;
    var upplimit = 4;
    System.out.println ( "f(x) =" , round ( BooleRule ( 0 , 4 ) , 4 ) );
}
 