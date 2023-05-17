public void gcd ( a , b ) {
    if (( var a == 0 )) {
        return b;
    }
     return gcd ( b % a , a );
}
public void powGCD ( a , n , b ) {
    for i in range ( 0 , n + 1 , 1 ) :
        a = a * a;
    return gcd ( a , b );
}
if (__name__ == '__main__') {
    a = 10;
    var b = 5;
    var n = 2;
    System.out.println ( powGCD ( a , n , b ) );
}
 