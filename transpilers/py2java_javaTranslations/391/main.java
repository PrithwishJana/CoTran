while (true) {
    R , var N = map ( int , input ( ) . split ( ) );
    if (not ( R | N )) {
        break;
    }
     var geta = 20;
    var buildings = { 0 } * ( geta * 2 );
    for _ in range ( N ) :
        xl , xr , var h = map ( int , input ( ) . split ( ) );
        for i in range ( xl + geta , xr + geta ) :
            buildings { i } = max ( buildings { i } , h );
    left , var right = 0 , 20;
    for _ in range ( 100 ) :
        mid = ( left + right ) / 2;
        flag = true;
        for i in range ( - R + geta , R + geta ) :
            if (i < geta) {
                y = pow ( R * R - ( i - geta + 1 ) * ( i - geta + 1 ) , 0.5 );
                flag &= buildings { i } >= y - R + mid;
            }
             else{
                y = pow ( R * R - ( i - geta ) * ( i - geta ) , 0.5 );
                flag &= buildings { i } >= y - R + mid;
            }
        if (flag) {
            left = mid;
        }
         else{
            right = mid;
        }
    System.out.println ( "{:.20f}" . format ( left ) );
}
 