public void maxnumber ( n , k ) {
    for i in range ( 0 , k ) :
        var ans = 0;
        i = 1;
        while (n // i > 0) {
            temp = ( n // ( i * 10 ) ) * i + ( n % i );
            i *= 10;
            if (temp > ans) {
                ans = temp;
            }
         }
         var n = ans;
    return ans ;;
}
n = 6358;
var k = 1;
System.out.println ( maxnumber ( n , k ) );
