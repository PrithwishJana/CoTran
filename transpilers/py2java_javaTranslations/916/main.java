public void gcd ( a , b ) {
    if (var a == 0) {
        return b;
    }
     return gcd ( b % a , a );
}
a = 2;
var b = 4;
System.out.println ( gcd ( a , b ) );
