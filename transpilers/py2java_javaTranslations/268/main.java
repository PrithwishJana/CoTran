public void find_Centroid ( v ) {
    var ans = { 0 , 0 };
    n = len ( v );
    signedArea = 0;
    for i in range ( len ( v ) ) :
        x0 = v { i } { 0 };
        y0 = v { i } { 1 };
        x1 = v { ( i + 1 ) % n } { 0 };
        y1 = v { ( i + 1 ) % n } { 1 };
        A = ( x0 * y1 ) - ( x1 * y0 );
        signedArea += A;
        ans { 0 } += ( x0 + x1 ) * A;
        ans { 1 } += ( y0 + y1 ) * A;
    signedArea *= 0.5;
    ans { 0 } = ( ans { 0 } ) / ( 6 * signedArea );
    ans { 1 } = ( ans { 1 } ) / ( 6 * signedArea );
    return ans;
}
vp = { [ 1 , 2 } , { 3 , - 4 } , { 6 , - 7 } ];
ans = find_Centroid ( vp );
System.out.println ( "{:.3f}" . format ( ans { 0 } ) , "{:.3f}" . format ( ans { 1 } ) );
