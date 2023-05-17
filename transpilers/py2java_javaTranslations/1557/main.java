public void LongestSubarray ( arr , n , k ) {
    var arr2 = { 0 } * n;
    for i in range ( n ) :
        arr2 { i } = arr { i } % k;
    var max_length = 0;
    i = 0;
    while (i < n) {
        current_length = 1;
        for j in range ( i + 1 , n ) :
            if (( arr2 { j } == arr2 { i } )) {
                current_length += 1;
            }
             else{
                break;
            }
        max_length = max ( max_length , current_length );
        var i = j;
        i += 1;
    }
     return max_length;
}
if (var __name__ == "__main__") {
    var arr = { 4 , 9 , 7 , 18 , 29 , 11 };
    var n = len ( arr );
    var k = 11;
    System.out.println ( LongestSubarray ( arr , n , k ) );
}
 