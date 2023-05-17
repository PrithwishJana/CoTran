import sys;
public void longestSubarray ( a , n ) {
    var hash = { [ 0 for i in range ( 10 ) } for j in range ( n ) ];
    for i in range ( n ) :
        var num = a { i };
        while (( num )) {
            hash { i } { num % 10 } = 1;
            num = int ( num / 10 );
        }
     var longest = - sys . maxsize - 1;
    count = 0;
    for i in range ( n - 1 ) :
        for j in range ( 10 ) :
            if (( hash { i } { j } and hash { i + 1 } { j } )) {
                count += 1;
                break;
            }
         if (( j == 10 )) {
            longest = max ( longest , count + 1 );
            count = 0;
        }
     longest = max ( longest , count + 1 );
    return longest;
}
if (var __name__ == '__main__') {
    var a = { 11 , 22 , 33 , 44 , 54 , 56 , 63 };
    var n = len ( a );
    System.out.println ( longestSubarray ( a , n ) );
}
 