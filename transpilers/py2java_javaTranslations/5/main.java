var NUM = ( 0b0111111 , 0b0000110 , 0b1011011 , 0b1001111 , 0b1100110 , 0b1101101 , 0b1111101 , 0b0100111 , 0b1111111 , 0b1101111 , );
while (1) {
    var n = int ( input ( ) );
    if n == - 1 : break;
    var current = 0;
    for i in range ( n ) :
        num = NUM { int ( input ( ) ) };
        System.out.println ( format ( current ^ num , 'b' ) . zfill ( 7 ) );
        current = num;
}
 