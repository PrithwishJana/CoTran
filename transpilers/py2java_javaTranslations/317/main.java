public void compute ( ) {
    var ans = sum ( 1 for i in range ( 1 , 10000000 ) if get_terminal ( i ) == 89 );
    return str ( ans );
}
var TERMINALS = ( 1 , 89 );
public void get_terminal ( n ) {
    while (n not in TERMINALS) {
        var n = square_digit_sum ( n );
    }
     return n;
}
public void square_digit_sum ( n ) {
    var result = 0;
    while (n > 0) {
        result += SQUARE_DIGITS_SUM { n % 1000 };
        n //= 1000;
    }
     return result;
}
var SQUARE_DIGITS_SUM = { sum ( int ( c ) ** 2 for c in str ( i ) ) for i in range ( 1000 ) };
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 