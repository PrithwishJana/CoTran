while (true) {
    var X = input ( );
    if X == '0' : break;
    r = '';
    minus = false;
    if (X { 0 } == '-') {
        minus = true;
        X = X { 1 : };
    }
     kuri = 0;
    idx = len ( X ) - 1;
    while (idx >= 0) {
        a = int ( X { idx } );
        if (minus) {
            r = str ( ( 10 - a - kuri ) % 10 ) + r;
            kuri = 0 if kuri + a == 0 else 1;
        }
         else{
            r = str ( ( kuri + a ) % 10 ) + r;
            kuri = ( kuri + a ) // 10;
        }
        minus = not minus;
        if (idx == 0 and kuri > 0) {
            X = '0' + X;
        }
         else{
            idx -= 1;
        }
    }
     var r = str ( kuri ) + r;
    System.out.println ( int ( r ) );
}
 