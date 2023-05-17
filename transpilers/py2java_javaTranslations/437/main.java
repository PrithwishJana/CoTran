public void findSubSequence ( s , num ) {
    var res = 0;
    var i = 0;
    while (( num )) {
        if (( num & 1 )) {
            res += ord ( s { i } ) - ord ( '0' );
        }
         i += 1;
        var num = num >> 1;
    }
     return res;
}
public void combinedSum ( s ) {
    var n = len ( s );
    c_sum = 0;
    ran = ( 1 << n ) - 1;
    for i in range ( ran + 1 ) :
        c_sum += findSubSequence ( s , i );
    return c_sum;
}
if (var __name__ == "__main__") {
    var s = "123";
    System.out.println ( combinedSum ( s ) );
}
 