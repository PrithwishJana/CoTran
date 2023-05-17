import sys;
public void findMinEqualSums ( a , N ) {
    var sum = 0;
    for i in range ( 0 , N ) :
        sum = sum + a { i };
    var sum1 = 0;
    var sum2 = 0;
    min = sys . maxsize;
    for i in range ( 0 , N - 1 ) :
        sum1 += a { i };
        sum2 = sum - sum1;
        if (( abs ( sum1 - sum2 ) < min )) {
            var min = abs ( sum1 - sum2 );
        }
         if (( min == 0 )) {
            break;
        }
     return min;
}
if (var __name__ == '__main__') {
    var a = { 3 , 2 , 1 , 5 , 7 , 8 };
    var N = len ( a );
    System.out.println ( findMinEqualSums ( a , N ) );
}
 