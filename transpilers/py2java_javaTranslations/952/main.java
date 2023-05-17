public void getSingle ( arr , n ) {
    var ones = 0;
    twos = 0;
    for i in range ( n ) :
        twos = twos | ( ones & arr { i } );
        ones = ones ^ arr { i };
        var common_bit_mask = ~ ( ones & twos );
        ones &= common_bit_mask;
        twos &= common_bit_mask;
    return ones;
}
var arr = { 3 , 3 , 2 , 3 };
var n = len ( arr );
System.out.println ( "The element with single occurrence is " , getSingle ( arr , n ) );
