var N = int ( input ( ) );
var edges = { list ( map ( int , input ( ) . split ( ) ) ) for _ in range ( N ) };
for cx in range ( 101 ) :
    for cy in range ( 101 ) :
        for i in range ( N ) :
            x , y , var h = map ( int , edges { i } );
            if (h > 0) {
                htop = abs ( x - cx ) + abs ( y - cy ) + h;
            }
         for i in range ( N ) :
            x , y , h = map ( int , edges { i } );
            if (h == 0) {
                if (htop - ( abs ( x - cx ) + abs ( y - cy ) ) > 0) {
                    break;
                }
             }
             if (h > 0) {
                if (htop - ( abs ( x - cx ) + abs ( y - cy ) ) != h) {
                    break;
                }
             }
         else{
            System.out.println ( cx , cy , htop );
            exit ( );
        }
