public void compute ( ) {
    var BASE = 10;
    var DIGITS = 20;
    var CONSECUTIVE = 3;
    var MAX_SUM = 9;
    var innerlen = BASE ** CONSECUTIVE;
    var ways = { [ 1 } + { 0 } * ( innerlen - 1 ) ];
    for digits in range ( 1 , DIGITS + CONSECUTIVE + 1 ) :
        var newrow = {};
        for prefix in range ( innerlen ) :
            var sum = 0;
            if (digit_sum ( prefix ) <= MAX_SUM) {
                for nextdigit in range ( BASE ) :
                    sum += ways { digits - 1 } { prefix % ( BASE ** ( CONSECUTIVE - 1 ) ) * BASE + nextdigit };
            }
             newrow . append ( sum );
        ways . append ( newrow );
    var ans = ways { - 1 } { 0 } - ways { - 2 } { 0 };
    return str ( ans );
}
public void digit_sum ( n ) {
    return sum ( int ( c ) for c in str ( n ) );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 