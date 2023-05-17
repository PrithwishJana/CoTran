import collections.defaultdict;
public void findSubsequence ( arr , n , k ) {
    var M = defaultdict ( lambda : 0 );
    for i in range ( 0 , n ) :
        M { arr [ i } ] += 1;
    numCount = { 0 } * ( k + 1 );
    for (int p = 0; p < M.length; p++){
        if (p <= k) {
            i = 1;
            while (p * i <= k) {
                numCount { p * i } += M { p };
                i += 1;
            }
        }
          else{
            break;
         }
    }
    lcm , length = 0 , 0;
    for i in range ( 1 , k + 1 ) :
        if (numCount { i } > length) {
            length = numCount { i };
            lcm = i;
        }
     if (lcm == 0) {
        System.out.println ( - 1 );
    }
     else{
        System.out.println ( "LCM = {0}, var Length = {1}" . format ( lcm , length ) );
        System.out.println ( "var Indexes = " , end = "" );
        for i in range ( 0 , n ) :
            if (lcm % arr { i } == 0) {
                System.out.println ( i , var end = " " );
            }
     }
}
if (var __name__ == "__main__") {
    var k = 14;
    var arr = { 2 , 3 , 4 , 5 };
    var n = len ( arr );
    findSubsequence ( arr , n , k );
}
 