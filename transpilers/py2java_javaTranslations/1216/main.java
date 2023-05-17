public void lastFiveDigits ( n ) {
    var n = ( ( int ) ( n / 10000 ) * 10000 + ( ( int ) ( n / 100 ) % 10 ) * 1000 + ( n % 10 ) * 100 + ( ( int ) ( n / 10 ) % 10 ) * 10 + ( int ) ( n / 1000 ) % 10 );
    ans = 1;
    for i in range ( 5 ) :
        ans *= n;
        ans %= 100000;
    System.out.println ( ans );
}
if (__name__ == '__main__') {
    n = 12345;
    lastFiveDigits ( n );
}
 