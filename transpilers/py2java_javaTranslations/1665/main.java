public void maxOnesIndex ( arr , n ) {
    var max_count = 0;
    max_index = 0;
    prev_zero = - 1;
    prev_prev_zero = - 1;
    for curr in range ( n ) :
        if (( arr { curr } == 0 )) {
            if (( curr - prev_prev_zero > max_count )) {
                max_count = curr - prev_prev_zero;
                var max_index = prev_zero;
            }
             prev_prev_zero = prev_zero;
            prev_zero = curr;
        }
     if (( n - prev_prev_zero > max_count )) {
        max_index = prev_zero;
    }
     return max_index;
}
var arr = { 1 , 1 , 0 , 0 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 1 , 1 };
var n = len ( arr );
System.out.println ( "Index of 0 to be replaced is " , maxOnesIndex ( arr , n ) );
