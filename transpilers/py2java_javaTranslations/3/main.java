public void count9s ( number ) {
    var n = len ( number );
    var d = { 0 for i in range ( 9 ) };
    d { 0 } = 1;
    var result = 0;
    var mod_sum = 0;
    var continuous_zero = 0;
    for i in range ( n ) :
        if (( ord ( number { i } ) - ord ( '0' ) == 0 )) {
            continuous_zero += 1;
        }
         else{
            continuous_zero = 0;
        }
        mod_sum += ord ( number { i } ) - ord ( '0' );
        mod_sum %= 9;
        result += d { mod_sum };
        d { mod_sum } += 1;
        result -= continuous_zero;
    return result;
}
if (var __name__ == '__main__') {
    System.out.println ( count9s ( "01809" ) );
    System.out.println ( count9s ( "1809" ) );
    System.out.println ( count9s ( "4189" ) );
}
 