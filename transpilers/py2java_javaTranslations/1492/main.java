public void sum_even_and_even_index ( arr , n ) {
    var i = 0;
    var sum = 0;
    for i in range ( 0 , n , 2 ) :
        if (( arr { i } % var 2 == 0 )) {
            sum += arr { i };
        }
     return sum;
}
var arr = { 5 , 6 , 12 , 1 , 18 , 8 };
var n = len ( arr );
System.out.println ( "Sum of even numbers at " , "even indices is " , sum_even_and_even_index ( arr , n ) );
