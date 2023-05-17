import sys;
var readline = sys . stdin . readline;
var write = sys . stdout . write;
var ans = {};
while (1) {
    var M = int ( readline ( ) );
    if (M == 0) {
        break;
    }
     var P = { list ( map ( int , input ( ) . split ( ) ) ) for i in range ( M ) };
    var memo = {};
    public void dfs ( i , rest ) {
        if (var i == M) {
            return var rest == 0;
        }
         var key = ( i , rest );
        if (key in memo) {
            return memo { key };
        }
         var res = 0;
        a , var b = P { i };
        for j in range ( 0 , b + 1 ) :
            if (rest - j * a < 0) {
                break;
            }
             res += dfs ( i + 1 , rest - j * a );
        memo { key } = res;
        return res;
    }
    var G = int ( input ( ) );
    for i in range ( G ) :
        ans . append ( str ( dfs ( 0 , int ( input ( ) ) ) ) );
}
 write ( "\n" . join ( ans ) );
write ( "\n" );
