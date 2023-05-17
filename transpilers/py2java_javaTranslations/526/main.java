while (true) {
    var balls = int ( input ( ) );
    ans = 0;
    if (balls == 0) {
        break;
    }
     for cs in range ( 54 ) :
        for ts in range ( 96 ) :
            if (pow ( cs , 3 ) <= balls) {
                var ans = max ( ans , pow ( cs , 3 ) );
            }
             if (ts * ( ts + 1 ) * ( ts + 2 ) // 6 <= balls) {
                ans = max ( ans , ts * ( ts + 1 ) * ( ts + 2 ) // 6 );
            }
             if (pow ( cs , 3 ) + ts * ( ts + 1 ) * ( ts + 2 ) // 6 <= balls) {
                ans = max ( ans , pow ( cs , 3 ) + ts * ( ts + 1 ) * ( ts + 2 ) // 6 );
            }
     System.out.println ( ans );
}
 