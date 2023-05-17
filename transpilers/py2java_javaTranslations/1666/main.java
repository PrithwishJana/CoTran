public void minimumX ( n , k ) {
    var ans = 10 ** 18;
    for i in range ( k - 1 , 0 , - 1 ) :
        if (n % i == 0) {
            ans = min ( ans , i + ( n / i ) * k );
        }
     return ans;
}
n , var k = 4 , 6;
System.out.println ( minimumX ( n , k ) );
n , k = 5 , 5;
System.out.println ( minimumX ( n , k ) );
