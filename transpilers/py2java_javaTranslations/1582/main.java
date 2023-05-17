public void maxDiff ( arr , n ) {
    var diff = arr { 1 } - arr { 0 };
    curr_sum = diff;
    max_sum = curr_sum;
    for i in range ( 1 , n - 1 ) :
        diff = arr { i + 1 } - arr { i };
        if (( curr_sum > 0 )) {
            curr_sum += diff;
        }
         else{
            var curr_sum = diff;
        }
        if (( curr_sum > max_sum )) {
            var max_sum = curr_sum;
        }
     return max_sum;
}
if (var __name__ == '__main__') {
    var arr = { 80 , 2 , 6 , 3 , 100 };
    var n = len ( arr );
    System.out.println ( "Maximum difference is" , maxDiff ( arr , n ) );
}
 