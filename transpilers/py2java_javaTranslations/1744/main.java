public void findKthChar ( s , k ) {
    var len1 = len ( s );
    var i = 0;
    var total_len = 0;
    while (( i < len1 )) {
        if (( s { i } . isalpha ( ) )) {
            total_len += 1;
            if (( total_len == k )) {
                return s { i };
            }
             i += 1;
        }
         else{
            n = 0;
            while (( i < len1 and s { i } . isalpha ( ) == false )) {
                n = n * 10 + ( ord ( s { i } ) - ord ( '0' ) );
                i += 1;
            }
             next_total_len = total_len * n;
            if (( k <= next_total_len )) {
                pos = k % total_len;
                if (( pos == 0 )) {
                    pos = total_len;
                }
                 return findKthChar ( s , pos );
            }
             else{
                total_len = next_total_len;
            }
        }
    }
     return - 1;
}
if (var __name__ == '__main__') {
    var s = "ab2c3";
    var k = 5;
    System.out.println ( findKthChar ( s , k ) );
}
 