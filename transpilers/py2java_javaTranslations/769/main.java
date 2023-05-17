public void sum ( x , y , n ) {
    var sum1 = ( ( x ** 2 ) * ( x ** ( 2 * n ) - 1 ) ) // ( x ** 2 - 1 );
    var sum2 = ( x * y * ( x ** n * y ** n - 1 ) ) // ( x * y - 1 );
    return ( sum1 + sum2 );
}
if (var __name__ == '__main__') {
    var x = 2;
    var y = 2;
    var n = 2;
    System.out.println ( sum ( x , y , n ) );
}
 