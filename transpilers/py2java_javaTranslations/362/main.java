protected void gcd ( a , b ) {
    if (( var a == 0 or b == 0 )) {
        return 0;
    }
     if (( a == b )) {
        return a;
    }
     if (( a > b )) {
        return __gcd ( a - b , b );
    }
     return __gcd ( a , b - a );
}
public void findValue ( x , y , z ) {
    var g = __gcd ( y , z );
    return ( x * g ) / __gcd ( x , g );
}
var x = 30;
var y = 40;
var z = 400;
System.out.println ( "%d" % findValue ( x , y , z ) );
