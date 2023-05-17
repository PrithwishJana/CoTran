public void isPrime ( n , var i = 2 ) {
    if (( n <= 2 )) {
        return true if ( n == 2 ) else false;
    }
     if (( n % i == 0 )) {
        return false;
    }
     if (( i * i > n )) {
        return true;
    }
     return isPrime ( n , i + 1 );
}
var n = 15;
if (( isPrime ( n ) )) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
