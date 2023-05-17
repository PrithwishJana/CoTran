public void countDistictSubarray ( arr , n ) {
    var vis = dict ( );
    for i in range ( n ) :
        vis { arr [ i } ] = 1;
    var k = len ( vis );
    var vid = dict ( );
    var ans = 0;
    var right = 0;
    var window = 0;
    for left in range ( n ) :
        while (( right < n and window < k )) {
            if (arr { right } in vid . keys ( )) {
                vid { arr [ right } ] += 1;
            }
             else{
                vid { arr [ right } ] = 1;
            }
            if (( vid { arr [ right } ] == 1 )) {
                window += 1;
            }
             right += 1;
        }
         if (( window == k )) {
            ans += ( n - right + 1 );
         }
         vid { arr [ left } ] -= 1;
        if (( vid { arr [ left } ] == 0 )) {
            window -= 1;
        }
     return ans;
}
var arr = { 2 , 1 , 3 , 2 , 3 };
var n = len ( arr );
System.out.println ( countDistictSubarray ( arr , n ) );
