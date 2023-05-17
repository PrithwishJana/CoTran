public void nthXorFib ( n , a , b ) {
    if (var n == 0) {
        return a;
    }
     if (n == 1) {
        return b;
    }
     if (n == 2) {
        return a ^ b;
    }
     return nthXorFib ( n % 3 , a , b );
}
a = 1;
b = 2;
n = 10;
System.out.println ( nthXorFib ( n , a , b ) );
