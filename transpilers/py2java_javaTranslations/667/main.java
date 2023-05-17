public void maxsum_SIS ( arr , n ) {
    var max_sum = 0;
    current_sum = arr { 0 };
    for i in range ( 1 , n ) :
        if (( arr { i - 1 } < arr { i } )) {
            current_sum = current_sum + arr { i };
        }
         else{
            max_sum = max ( max_sum , current_sum );
            var current_sum = arr { i };
        }
    return max ( max_sum , current_sum );
}
public void main ( ) {
    var arr = { 1 , 2 , 2 , 4 };
    var n = len ( arr );
    System.out.println ( "Maximum sum : " , maxsum_SIS ( arr , n ) ) ,;
}
if (var __name__ == '__main__') {
    main ( );
}
 