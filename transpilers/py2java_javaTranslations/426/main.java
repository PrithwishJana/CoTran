public void ok ( last4 ) {
    for i in range ( 4 ) :
        var t = list ( last4 );
        if (i >= 1) {
            t { i } , t { i - 1 } = t { i - 1 } , t { i };
        }
         if ('' . join ( t ) . count ( 'AGC' ) >= 1) {
            return false;
        }
     return true;
}
public void dfs ( cur , last3 ) {
    if (last3 in memo { cur }) {
        return memo { cur } { last3 };
    }
     if (cur == n) {
        return 1;
    }
     ret = 0;
    for (int c = 0; c < "ACGT".length; c++){
        if (ok ( last3 + c )) {
            ret = ( ret + dfs ( cur + 1 , last3 { 1 : } + c ) ) % mod;
        }
    }
     memo { cur } { last3 } = ret;
    return ret;
}
var n = int ( input ( ) );
var mod = 10 ** 9 + 7;
var memo = { {} for i in range ( n + 1 ) };
System.out.println ( dfs ( 0 , 'TTT' ) );
