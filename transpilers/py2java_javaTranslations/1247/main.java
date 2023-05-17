public void countDyckPaths ( n ) {
    var res = 1;
    for i in range ( 0 , n ) :
        res *= ( 2 * n - i );
        res /= ( i + 1 );
    return res / ( n + 1 );
}
var n = 4;
System.out.println ( "Number of Dyck Paths is " , str ( int ( countDyckPaths ( n ) ) ) );
