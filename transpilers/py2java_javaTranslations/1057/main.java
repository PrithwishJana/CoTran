public void countMaxContiguous ( arr , n ) {
    var current_max = 0;
    max_so_far = 0;
    for i in range ( n ) :
        if (( arr { i } % 2 != 0 )) {
            current_max = 0;
        }
         else{
            current_max += 1;
            var max_so_far = max ( current_max , max_so_far );
        }
    return max_so_far;
}
if (var __name__ == "__main__") {
    var arr = { 1 , 0 , 2 , 4 , 3 , 8 , 9 };
    var n = len ( arr );
    System.out.println ( countMaxContiguous ( arr , n ) );
}
 