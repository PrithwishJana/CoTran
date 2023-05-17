import collections.defaultdict;
var MAX_CHARS = 256;
public void findSubString ( strr ) {
    var n = len ( strr );
    if (n <= 1) {
        return strr;
    }
     dist_count = len ( set ( { x for x in strr } ) );
    curr_count = defaultdict ( lambda : 0 );
    count = 0;
    start = 0;
    min_len = n;
    for j in range ( n ) :
        curr_count { strr [ j } ] += 1;
        if (curr_count { strr [ j } ] == 1) {
            count += 1;
        }
         if (count == dist_count) {
            while (curr_count { strr [ start } ] > 1) {
                if (curr_count { strr [ start } ] > 1) {
                    curr_count { strr [ start } ] -= 1;
                }
                 start += 1;
            }
             len_window = j - start + 1;
            if (min_len > len_window) {
                min_len = len_window;
                var start_index = start;
            }
         }
     return str ( strr { start_index : start_index + min_len } );
}
if (var __name__ == '__main__') {
    System.out.println ( "Smallest window containing " "all distinct characters is: {}" . format ( findSubString ( "aabcbcdbca" ) ) );
}
 