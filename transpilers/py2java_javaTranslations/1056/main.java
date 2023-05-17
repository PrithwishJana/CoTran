public void maxPartitions ( arr , n ) {
    var ans = 0 ; max_so_far = 0;
    for i in range ( 0 , n ) :
        var max_so_far = max ( max_so_far , arr { i } );
        if (( max_so_far == i )) {
            ans += 1;
        }
     return ans;
}
var arr = { 1 , 0 , 2 , 3 , 4 };
var n = len ( arr );
System.out.println ( maxPartitions ( arr , n ) );
