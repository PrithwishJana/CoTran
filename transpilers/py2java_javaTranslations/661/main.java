public void findAnswer ( n , arr ) {
    arr . sort ( var reverse = false );
    var sum = 0;
    for i in range ( int ( n / 2 ) ) :
        sum += ( ( arr { i } + arr { n - i - 1 } ) * ( arr { i } + arr { n - i - 1 } ) );
    return sum;
}
if (var __name__ == '__main__') {
    var arr = { 53 , 28 , 143 , 5 };
    var n = len ( arr );
    System.out.println ( findAnswer ( n , arr ) );
}
 