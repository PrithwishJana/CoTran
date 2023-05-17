var mod = 1000000007;
public void digitNumber ( n ) {
    if (( var n == 0 )) {
        return 1;
    }
     if (( n == 1 )) {
        return 9;
    }
     if (( n % 2 != 0 )) {
        temp = digitNumber ( ( n - 1 ) // 2 ) % mod;
        return ( 9 * ( temp * temp ) % mod ) % mod;
    }
     else{
        temp = digitNumber ( n // 2 ) % mod;
        return ( temp * temp ) % mod;
    }
}
public void countExcluding ( n , d ) {
    if (( d == 0 )) {
        return ( 9 * digitNumber ( n - 1 ) ) % mod;
    }
     else{
        return ( 8 * digitNumber ( n - 1 ) ) % mod;
    }
}
d = 9;
n = 3;
System.out.println ( countExcluding ( n , d ) );
