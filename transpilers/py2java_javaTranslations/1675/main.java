public void maxDiff ( arr , arr_size ) {
    var max_diff = arr { 1 } - arr { 0 };
    min_element = arr { 0 };
    for i in range ( 1 , arr_size ) :
        if (( arr { i } - min_element > max_diff )) {
            max_diff = arr { i } - min_element;
        }
         if (( arr { i } < min_element )) {
            var min_element = arr { i };
        }
     return max_diff;
}
var arr = { 1 , 2 , 6 , 80 , 100 };
var size = len ( arr );
System.out.println ( "Maximum difference is" , maxDiff ( arr , size ) );
