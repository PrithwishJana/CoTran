public void isDivisible ( n ) {
    while (n // 100) {
        var d = n % 10;
        n //= 10;
        var n = abs ( n - ( d * 3 ) );
    }
     return ( n % 31 == 0 );
}
if (__name__ == "__main__") {
    n = 1922;
    if (( isDivisible ( n ) )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
}
 