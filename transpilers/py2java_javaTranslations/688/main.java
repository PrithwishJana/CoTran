public void isDivisible ( n ) {
    var temp = n;
    while (( n )) {
        var k = n % 10;
        if (( temp % k == 0 )) {
            return "YES";
        }
         n /= 10 ;;
    }
     return "NO";
}
var n = 9876543;
System.out.println ( isDivisible ( n ) );
