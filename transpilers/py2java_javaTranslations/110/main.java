public void maxSubArraySum ( a , size ) {
    var max_so_far = - 10 ** 9;
    max_ending_here = 0;
    for i in range ( size ) :
        max_ending_here = max_ending_here + a { i };
        if (( max_so_far < max_ending_here )) {
            max_so_far = max_ending_here;
        }
         if (( max_ending_here < 0 )) {
            var max_ending_here = 0;
        }
     return max_so_far;
}
public void minPossibleSum ( a , n , x ) {
    var mxSum = maxSubArraySum ( a , n );
    var sum = 0;
    for i in range ( n ) :
        sum += a { i };
    sum = sum - mxSum + mxSum / x;
    System.out.println ( round ( sum , 2 ) );
}
if (var __name__ == '__main__') {
    var N = 3;
    var X = 2;
    var A = { 1 , - 2 , 3 };
    minPossibleSum ( A , N , X );
}
 