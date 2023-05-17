public void maxSubArraySum ( arr , size ) {
    var max_so_far = arr { 0 };
    curr_max = arr { 0 };
    for i in range ( 1 , size ) :
        curr_max = max ( arr { i } , curr_max + arr { i } );
        max_so_far = max ( max_so_far , curr_max );
    return max_so_far;
}
public void lenOfLongSubarrWithGivenSum ( arr , n , k ) {
    var um = dict ( );
    Sum , maxLen = 0 , 0;
    for i in range ( n ) :
        Sum += arr { i };
        if (( Sum == k )) {
            maxLen = i + 1;
        }
         if (( Sum not in um . keys ( ) )) {
            um { Sum } = i;
        }
         if (( Sum in um . keys ( ) )) {
            if (( ( Sum - k ) in um . keys ( ) and maxLen < ( i - um { Sum - k } ) )) {
                maxLen = i - um { Sum - k };
            }
         }
     return maxLen;
}
public void lenLongSubarrWithMaxSum ( arr , n ) {
    maxSum = maxSubArraySum ( arr , n );
    return lenOfLongSubarrWithGivenSum ( arr , n , maxSum );
}
arr = { 5 , - 2 , - 1 , 3 , - 4 };
n = len ( arr );
System.out.println ( "Length of longest subarray having maximum sum =" , lenLongSubarrWithMaxSum ( arr , n ) );
