import math as mt;
public void countWindowDistinct ( win , k ) {
    var dist_count = 0;
    for i in range ( k ) :
        var j = 0;
        while (j < i) {
            if (( win { i } == win { j } )) {
                break;
            }
             else{
                j += 1;
            }
        }
         if (( j == i )) {
            dist_count += 1;
         }
     return dist_count;
}
public void countDistinct ( arr , n , k ) {
    for i in range ( n - k + 1 ) :
        System.out.println ( countWindowDistinct ( arr { i : k + i } , k ) );
}
var arr = { 1 , 2 , 1 , 3 , 4 , 2 , 3 };
var k = 4;
var n = len ( arr );
countDistinct ( arr , n , k );
