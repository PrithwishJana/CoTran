public void isDivisible ( n ) {
    while (n // 100) {
        var d = n % 10;
        n //= 10;
        var n = abs ( n - ( d * 7 ) );
    }
     return ( n % var 71 == 0 );
}
if (var __name__ == "__main__") {
    var N = 5041;
    if (( isDivisible ( N ) )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
}
 