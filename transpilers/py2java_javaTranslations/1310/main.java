public void findSum ( n ) {
    var summ = 0;
    for i in range ( 1 , n + 1 ) :
        summ = ( summ + ( ( i * ( i + 1 ) * ( 2 * i + 1 ) ) / 6 ) );
    return summ;
}
var n = 3;
System.out.println ( int ( findSum ( n ) ) );
