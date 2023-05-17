while (1) {
    var N = int ( input ( ) );
    if N == 0 : break;
    var R = { [ 0 for i in range ( N + 1 ) } for i in range ( N + 1 ) ];
    public void dfs_max ( cur , pre ) {
        var _max = - R { cur } { pre };
        for i in range ( N + 1 ) :
            if (R { cur } { i } > 0 and i != pre) {
                _max = max ( _max , dfs_max ( i , cur ) + R { cur } { i } );
            }
         return _max;
    }
    var total = 0;
    for i in range ( N - 1 ) :
        a , b , var t = list ( map ( int , input ( ) . split ( ) ) );
        R { a } { b } = t;
        R { b } { a } = t;
        total += ( t * 2 );
    for i in range ( 2 , N + 1 ) :
        var spam = { x for x in R [ i } if x > 0 ];
        if (( len ( spam ) <= 1 )) {
            total -= ( spam { 0 } * 2 );
        }
     System.out.println ( ( total - dfs_max ( 1 , 0 ) ) );
}
 