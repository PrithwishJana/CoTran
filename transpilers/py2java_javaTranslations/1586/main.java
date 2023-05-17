public void solve ( ) {
    import sys.stdin;
    var f_i = stdin;
    public void rec ( i ) {
        if (var i == 0) {
            return 0;
        }
         var tray = cups { n - i };
        if (tray == 'A') {
            return rec ( i - 1 );
        }
         else if (tray == 'B'){
            return 2 * 3 ** ( i - 1 ) - 1 - rec ( i - 1 );
        }
        else{
            return rec ( i - 1 ) + 2 * 3 ** ( i - 1 );
        }
    }
    while (true) {
        n , var m = map ( int , f_i . readline ( ) . split ( ) );
        if (n == 0) {
            break;
        }
         cups = { None } * n;
        for (int tray = 0; tray < 'ABC'.length; tray++){
            itr = map ( int , f_i . readline ( ) . split ( ) );
            next ( itr );
            for (int i = 0; i < itr.length; i++){
                cups { i - 1 } = tray;
            }
        }
        num = rec ( n );
        var ans = min ( num , 3 ** n - 1 - num );
        if (ans <= m) {
            System.out.println ( ans );
        }
         else{
            System.out.println ( - 1 );
        }
    }
 }
solve ( );
