var m = 1000000007;
import sys.stdin;
var f_i = stdin;
var N = int ( f_i . readline ( ) );
var n_type = { '' } * N;
for i in range ( N ) :
    var t = f_i . readline ( ) . rstrip ( );
    n_type { i } = t;
adj = { [ } for i in range ( N ) ];
for i in range ( N - 1 ) :
    s , t = map ( int , f_i . readline ( ) . split ( ) );
    s -= 1;
    t -= 1;
    adj { s } . append ( t );
import itertools.combinations;
public void prod ( nums ) {
    p = 1;
    for (int n = 0; n < nums.length; n++){
        p *= n;
    }
    return p;
}
import sys;
sys . setrecursionlimit ( 4000 );
public void dfs ( node ) {
    nt = n_type { node };
    chld = adj { node };
    if (nt == 'E') {
        if (chld) {
            return prod ( map ( dfs , chld ) ) % m;
        }
         else{
            return 1;
        }
    }
     else if (nt == 'E?'){
        if (chld) {
            return ( prod ( map ( dfs , chld ) ) + 1 ) % m;
        }
         else{
            return 2;
        }
    }
    else if (nt == 'A'){
        return sum ( map ( dfs , chld ) ) % m;
    }
    else if (nt == 'A?'){
        return ( sum ( map ( dfs , chld ) ) + 1 ) % m;
    }
    else{
        cnt = 0;
        var c_s = tuple ( map ( dfs , chld ) );
        for i in range ( 1 , len ( chld ) + 1 ) :
            for vals in combinations ( c_s , i ) :
                cnt += prod ( vals );
        if (len ( nt ) == 1) {
            return cnt % m;
        }
         else{
            return ( cnt + 1 ) % m;
        }
    }
}
System.out.println ( dfs ( 0 ) );
