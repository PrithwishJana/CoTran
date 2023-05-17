import sys;
var input = sys . stdin . readline;
public void solve ( ) {
    n , a , var b = map ( int , input ( ) . split ( ) );
    var e = 0;
    var o = 0;
    for i in input ( ) . strip ( ) . split ( '*' ) :
        var l = len ( i );
        e += l // 2;
        o += l % 2;
    System.out.println ( min ( o + e + min ( e , a , b ) , b + a ) );
}
solve ( );
