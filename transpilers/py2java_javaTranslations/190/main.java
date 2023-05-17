var MOD = 1000000007;
public void countStrings ( N ) {
    var dp = { [ 0 } * 3 for i in range ( N + 1 ) ];
    dp { 1 } { 0 } = 1 ;;
    dp { 1 } { 1 } = 1 ;;
    dp { 1 } { 2 } = 0 ;;
    for i in range ( 2 , N + 1 ) :
        dp { i } { 0 } = ( dp { i - 1 } { 0 } + dp { i - 1 } { 1 } + dp { i - 1 } { 2 } ) % MOD;
        dp { i } { 1 } = dp { i - 1 } { 0 } % MOD;
        dp { i } { 2 } = dp { i - 1 } { 1 } % MOD;
    var ans = ( dp { N } { 0 } + dp { N } { 1 } + dp { N } { 2 } ) % MOD;
    return ans;
}
if (var __name__ == '__main__') {
    var N = 3;
    System.out.println ( countStrings ( N ) );
}
 