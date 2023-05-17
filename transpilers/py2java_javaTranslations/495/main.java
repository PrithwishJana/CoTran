public void findUniquePair ( arr , n ) {
    var XOR = arr { 0 };
    for i in range ( 1 , n ) :
        XOR = XOR ^ arr { i };
    var set_bit_no = XOR & ~ ( XOR - 1 );
    var x = 0;
    y = 0;
    for i in range ( 0 , n ) :
        if (( arr { i } & set_bit_no )) {
            x = x ^ arr { i };
        }
         else{
            var y = y ^ arr { i };
        }
    System.out.println ( "The unique pair is (" , x , ", " , y , ")" , var sep = "" );
}
var a = { 6 , 1 , 3 , 5 , 1 , 3 , 7 , 6 };
var n = len ( a );
findUniquePair ( a , n );
