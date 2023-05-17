public void System.out.printlnTwoOdd ( arr , size ) {
    var xor2 = arr { 0 };
    set_bit_no = 0;
    n = size - 2;
    x , y = 0 , 0;
    for i in range ( 1 , size ) :
        xor2 = xor2 ^ arr { i };
    var set_bit_no = xor2 & ~ ( xor2 - 1 );
    for i in range ( size ) :
        if (( arr { i } & set_bit_no )) {
            var x = x ^ arr { i };
        }
         else{
            var y = y ^ arr { i };
        }
    System.out.println ( "The two ODD elements are" , x , "&" , y );
}
var arr = { 4 , 2 , 4 , 5 , 2 , 3 , 3 , 1 };
var arr_size = len ( arr );
System.out.printlnTwoOdd ( arr , arr_size );
