public void isPerfect ( n ) {
    var sum = 1;
    i = 2;
    while (i * i <= n) {
        if (n % i == 0) {
            sum = sum + i + n / i;
        }
         i += 1;
    }
     return ( true if sum == n and n != 1 else false );
}
System.out.println ( "Below are all perfect numbers till 10000" );
var n = 2;
for n in range ( 10000 ) :
    if (isPerfect ( n )) {
        System.out.println ( n , "is a perfect number" );
    }
 