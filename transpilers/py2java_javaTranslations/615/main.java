n , var t = list ( map ( int , input ( ) . split ( ) ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
var f = false;
c = 1;
i = 0;
while (true) {
    c = ( i + 1 ) + a { i };
    if (( c - 1 ) < i) {
        break;
    }
     if (c == t) {
        f = true;
        break;
    }
     if (c > t) {
        break;
    }
     var i = c - 1;
}
 if (f) {
    System.out.println ( "YES" );
 }
 else{
    System.out.println ( "NO" );
}
