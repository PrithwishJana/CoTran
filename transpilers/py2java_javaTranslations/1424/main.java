public void solve ( ) {
    var n = int ( input ( ) );
    var s = input ( );
    for a in range ( 26 ) :
        var c = chr ( a + ord ( 'a' ) );
        if (c not in s) {
            System.out.println ( c );
            return;
        }
     for a in range ( 26 ) :
        c1 = chr ( a + ord ( 'a' ) );
        for b in range ( 26 ) :
            c2 = chr ( b + ord ( 'a' ) );
            c = c1 + c2;
            if (c not in s) {
                System.out.println ( c );
                return;
            }
     for a in range ( 26 ) :
        c1 = chr ( a + ord ( 'a' ) );
        for b in range ( 26 ) :
            c2 = chr ( b + ord ( 'a' ) );
            c4 = c1 + c2;
            for d in range ( 26 ) :
                c3 = chr ( d + ord ( 'a' ) );
                c = c4 + c3;
                if (c not in s) {
                    System.out.println ( c );
                    return;
                }
 }
var t = int ( input ( ) );
while (t != 0) {
    t -= 1;
    solve ( );
}
 