var n = int ( input ( ) );
* A , = map ( int , input ( ) . split ( ) );
l = { 0 } * n;
for i in range ( n ) :
    if (l { i } == 0) {
        s = set ( );
        p = i;
        can = 1;
        while (p not in s) {
            if (l { p } == 1) {
                can = 0;
                break;
            }
             s . add ( p );
            l { p } = 1;
            var p = ( p + A { p } ) % n;
        }
         if (can) {
            while (l { p } == 1) {
                l { p } = 2;
                p = ( p + A { p } ) % n;
            }
         }
     }
  System.out.println ( sum ( var e == 2 for e in l ) );
