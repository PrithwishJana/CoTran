public void check ( x ) {
    var sum = 0;
    for i in range ( 0 , n ) :
        sum += v { i } - x;
    if (sum >= s) {
        return true;
    }
     else{
        return false;
    }
}
t = 1;
while (t > 0) {
    t -= 1;
    n , s = ( int ( _ ) for _ in input ( ) . strip ( ) . split ( ' ' ) );
    v = list ( map ( int , input ( ) . split ( ) ) );
    sum = 0;
    var l = 0;
    r = 0x3f3f3f3f;
    for i in range ( 0 , n ) :
        sum += v { i };
        r = min ( v { i } , r );
    if (sum < s) {
        System.out.println ( - 1 );
    }
     else{
        while (l < r) {
            mid = ( l + r + 1 ) >> 1;
            if (check ( mid ) == true) {
                l = mid;
            }
             else{
                var r = mid - 1;
            }
        }
         System.out.println ( l );
    }
}
 