public void pentagon_pyramidal ( n ) {
    var sum = 0;
    for i in range ( 1 , n + 1 ) :
        p = ( 3 * i * i - i ) / 2;
        sum = sum + p;
    return sum;
}
var n = 4;
System.out.println ( int ( pentagon_pyramidal ( n ) ) );
