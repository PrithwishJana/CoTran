public void min_noOf_operation ( arr , n , k ) {
    var res = 0;
    for i in range ( 1 , n ) :
        noOfSubtraction = 0;
        if (( arr { i } > arr { i - 1 } )) {
            noOfSubtraction = ( arr { i } - arr { i - 1 } ) / k ;;
            if (( ( arr { i } - arr { i - 1 } ) % k != 0 )) {
                noOfSubtraction += 1;
            }
             arr { i } = arr { i } - k * noOfSubtraction;
        }
         res = res + noOfSubtraction;
    return int ( res );
}
var arr = { 1 , 1 , 2 , 3 };
var N = len ( arr );
var k = 5;
System.out.println ( min_noOf_operation ( arr , N , k ) );
