public void nthTerm ( n ) {
    var nth = 0;
    if (( n % 2 == 0 )) {
        nth = 2 * ( ( n * n ) - n );
    }
     else{
        nth = ( 2 * n * n ) - n;
    }
    return nth;
}
var n = 5;
System.out.println ( nthTerm ( n ) );
n = 25;
System.out.println ( nthTerm ( n ) );
n = 25000000;
System.out.println ( nthTerm ( n ) );
n = 250000007;
System.out.println ( nthTerm ( n ) );
