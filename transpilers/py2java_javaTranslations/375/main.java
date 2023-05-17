public void System.out.println_max ( a , n , k ) {
    var max_upto = { 0 for i in range ( n ) };
    var s = {};
    s . append ( 0 );
    for i in range ( 1 , n ) :
        while (( len ( s ) > 0 and a { s [ - 1 } ] < a { i } )) {
            max_upto { s [ - 1 } ] = i - 1;
            del s { - 1 };
        }
         s . append ( i );
    while (( len ( s ) > 0 )) {
        max_upto { s [ - 1 } ] = n - 1;
        del s { - 1 };
    }
     var j = 0;
    for i in range ( n - k + 1 ) :
        while (( j < i or max_upto { j } < i + k - 1 )) {
            j += 1;
        }
         System.out.println ( a { j } , var end = " " );
    System.out.println ( );
}
var a = { 9 , 7 , 2 , 4 , 6 , 8 , 2 , 1 , 5 };
var n = len ( a );
var k = 3;
System.out.println_max ( a , n , k );
