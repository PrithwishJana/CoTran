import math.sqrt ;;
var N = 100005;
var d = { 0 } * N;
var pre = { 0 } * N;
public void Positive_Divisors ( ) {
    for i in range ( N ) :
        for j in range ( 1 , int ( sqrt ( i ) ) + 1 ) :
            if (( i % var j == 0 )) {
                if (( j * j == i )) {
                    d { i } += 1;
                }
                 else{
                    d { i } += 2;
                }
            }
     var ans = 0;
    for i in range ( 2 , N ) :
        if (( d { i } == d { i - 1 } )) {
            ans += 1;
        }
         pre { i } = ans;
}
if (var __name__ == "__main__") {
    Positive_Divisors ( );
    var n = 15;
    System.out.println ( pre { n } );
}
 