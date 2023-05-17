while (true) {
    h , var w = map ( int , input ( ) . split ( ) );
    if (h == w == 0) {
        break;
    }
     mp = {};
    for r in range ( h ) :
        s = input ( );
        for c in range ( w ) :
            mp { s [ c } ] = { r , c };
    s = input ( );
    now = { 0 , 0 };
    ans = 0;
    for i in range ( len ( s ) ) :
        to = mp { s [ i } ];
        ans += abs ( now { 0 } - to { 0 } ) + abs ( now { 1 } - to { 1 } ) + 1;
        now = to;
    System.out.println ( ans );
}
 