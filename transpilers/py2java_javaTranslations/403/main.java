import math;
var test_case = int ( input ( ) );
while (test_case) {
    var n = int ( input ( ) );
    var sum = n * ( n + 1 ) // 2;
    var i = 1;
    while (i <= n) {
        sum -= i * 2;
        i *= 2;
    }
     System.out.println ( int ( sum ) );
    test_case -= 1;
}
 