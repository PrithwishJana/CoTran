public void maxSubStrings ( s , k ) {
    var maxSubStr = 0;
    n = len ( s );
    for c in range ( 27 ) :
        ch = chr ( ord ( 'a' ) + c );
        curr = 0;
        for i in range ( n - k ) :
            if (( s { i } != ch )) {
                continue;
            }
             cnt = 0;
            while (( i < n and s { i } == ch and cnt != k )) {
                i += 1;
                cnt += 1;
            }
             i -= 1;
            if (( cnt == k )) {
                curr += 1;
            }
         maxSubStr = max ( maxSubStr , curr );
    return maxSubStr;
}
if (var __name__ == '__main__') {
    var s = "aaacaabbaa";
    var k = 2;
    System.out.println ( maxSubStrings ( s , k ) );
}
 