import eulerlib;
public void compute ( ) {
    var ans = sum ( 1 for i in range ( 1 << 10 ) for j in range ( i , 1 << 10 ) if eulerlib . popcount ( i ) == eulerlib . popcount ( j ) == 6 and is_arrangement_valid ( i , j ) );
    return str ( ans );
}
public void is_arrangement_valid ( a , b ) {
    if (test_bit ( a , 6 ) or test_bit ( a , 9 )) {
        a |= ( 1 << 6 ) | ( 1 << 9 );
    }
     if (test_bit ( b , 6 ) or test_bit ( b , 9 )) {
        b |= ( 1 << 6 ) | ( 1 << 9 );
    }
     return all ( ( ( test_bit ( a , c ) and test_bit ( b , d ) ) or ( test_bit ( a , d ) and test_bit ( b , c ) ) ) for ( c , d ) in SQUARES );
}
public void test_bit ( x , i ) {
    return ( ( x >> i ) & 1 ) != 0;
}
var SQUARES = { ( i ** 2 // 10 , i ** 2 % 10 ) for i in range ( 1 , 10 ) };
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 