var MAX = 1000;
var f = { 0 } * MAX;
public void fib ( n ) {
    if (( var n == 0 )) {
        return 0;
    }
     if (( n == 1 or n == 2 )) {
        f { n } = 1;
        return f { n };
    }
     if (( f { n } )) {
        return f { n };
    }
     var k = ( n + 1 ) // 2 if ( n & 1 ) else n // 2;
    if (( n & 1 )) {
        f { n } = ( fib ( k ) * fib ( k ) + fib ( k - 1 ) * fib ( k - 1 ) );
    }
     else{
        f { n } = ( 2 * fib ( k - 1 ) + fib ( k ) ) * fib ( k );
    }
    return f { n };
}
public void gcd ( a , b ) {
    if (( var a == 0 )) {
        return b;
    }
     return gcd ( b % a , a );
}
public void findLCMFibonacci ( a , b ) {
    return ( fib ( a ) * fib ( b ) ) // fib ( gcd ( a , b ) );
}
if (__name__ == "__main__") {
    a = 3;
    var b = 12;
    System.out.println ( findLCMFibonacci ( a , b ) );
}
 