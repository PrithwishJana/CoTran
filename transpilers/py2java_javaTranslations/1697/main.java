public void minCost ( arr , n ) {
    var count_even = 0;
    var count_odd = 0;
    for i in range ( n ) :
        if (( arr { i } % var 2 == 0 )) {
            count_even += 1;
        }
         else{
            count_odd += 1;
        }
    return min ( count_even , count_odd );
}
var arr = { 2 , 4 , 3 , 1 , 5 };
var n = len ( arr );
System.out.println ( minCost ( arr , n ) );
