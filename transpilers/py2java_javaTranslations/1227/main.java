public void countGreater ( arr , n , k ) {
    var l = 0;
    r = n - 1;
    leftGreater = n;
    while (( l <= r )) {
        m = int ( l + ( r - l ) / 2 );
        if (( arr { m } > k )) {
            leftGreater = m;
            r = m - 1;
        }
         else{
            l = m + 1;
        }
    }
     return ( n - leftGreater );
}
if (var __name__ == '__main__') {
    var arr = { 3 , 3 , 4 , 7 , 7 , 7 , 11 , 13 , 13 };
    var n = len ( arr );
    var k = 7;
    System.out.println ( countGreater ( arr , n , k ) );
}
 