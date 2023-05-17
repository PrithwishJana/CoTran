public void check ( s ) {
    var freq = { 0 } * 10;
    while (( s != 0 )) {
        var r = s % 10;
        s = s // 10;
        freq { r } += 1;
    }
     xor = 0;
    for i in range ( 10 ) :
        xor = xor ^ freq { i };
    if (( xor == 0 )) {
        return true;
    }
     else{
        return false;
    }
}
var s = 122233;
if (( check ( s ) )) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
