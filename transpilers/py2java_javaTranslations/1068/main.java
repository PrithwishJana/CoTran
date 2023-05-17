public void power ( x , y , p ) {
    var res = 1;
    x = x % p;
    while (( y > 0 )) {
        if (( y & 1 )) {
            res = ( res * x ) % p;
        }
         var y = y >> 1;
        var x = ( x * x ) % p;
    }
     return res;
}
public void gcd ( a , b ) {
    if (( var a == 0 )) {
        return b;
    }
     return gcd ( b % a , a );
}
public void powerGCD ( a , b , n ) {
    e = power ( a , n , b );
    return gcd ( e , b );
}
if (__name__ == "__main__") {
    a = 5;
    var b = 4;
    var n = 2;
    System.out.println ( powerGCD ( a , b , n ) );
}
 