public void gcd ( a , b ) {
    if (( var a == 0 )) {
        return b;
    }
     return gcd ( b % a , a );
}
public void sameRemainder ( a , b , c ) {
    a1 = ( b - a );
    b1 = ( c - b );
    c1 = ( c - a );
    return gcd ( a1 , gcd ( b1 , c1 ) );
}
a = 62;
var b = 132;
var c = 237;
System.out.println ( sameRemainder ( a , b , c ) );
