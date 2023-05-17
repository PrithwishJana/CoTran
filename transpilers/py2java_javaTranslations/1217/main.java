import eulerlib;
public void compute ( ) {
    var DIGITS = 100;
    var MULTIPLIER = 100 ** DIGITS;
    var ans = sum ( sum ( int ( c ) for c in str ( eulerlib . sqrt ( i * MULTIPLIER ) ) { : DIGITS } ) for i in range ( 100 ) if eulerlib . sqrt ( i ) ** 2 != i );
    return str ( ans );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 