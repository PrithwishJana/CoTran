import sys.stdin;
var input = stdin . readline;
var inp = lambda : list ( map ( int , input ( ) . split ( ) ) );
public void answer ( a , b , c , d , e , f ) {
    if (( e > f )) {
        var m = min ( a , d );
        ans = e * m;
        d -= m;
        ans += f * min ( b , c , d );
    }
     else{
        m = min ( b , c , d );
        var ans = f * m;
        d -= m;
        ans += e * min ( a , d );
    }
    return ans;
}
for T in range ( 1 ) :
    var a = int ( input ( ) );
    var b = int ( input ( ) );
    var c = int ( input ( ) );
    var d = int ( input ( ) );
    var e = int ( input ( ) );
    var f = int ( input ( ) );
    System.out.println ( answer ( a , b , c , d , e , f ) );
