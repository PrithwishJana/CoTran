var M = 20;
var dp = {};
d , K = None , None;
public void count ( pos , cnt , tight , nonz , num : list ) {
    if (pos == len ( num )) {
        if (cnt == K) {
            return 1;
        }
         return 0;
    }
     if (dp { pos } { cnt } { tight } { nonz } != - 1) {
        return dp { pos } { cnt } { tight } { nonz };
    }
     ans = 0;
    limit = 9 if tight else num { pos };
    for dig in range ( limit + 1 ) :
        currCnt = cnt;
        if (dig == d) {
            if (d != 0 or not d and nonz) {
                currCnt += 1;
            }
         }
         currTight = tight;
        if (dig < num { pos }) {
            currTight = 1;
        }
         ans += count ( pos + 1 , currCnt , currTight , ( nonz or dig != 0 ) , num );
    dp { pos } { cnt } { tight } { nonz } = ans;
    return dp { pos } { cnt } { tight } { nonz };
}
public void solve ( x ) {
    global dp , K , d;
    num = {};
    while (x) {
        num . append ( x % 10 );
        x //= 10;
    }
     num . reverse ( );
    dp = { [ [ [ - 1 , - 1 } for i in range ( 2 ) ] for j in range ( M ) ] for k in range ( M ) ];
    return count ( 0 , 0 , 0 , 0 , num );
}
if (var __name__ == "__main__") {
    var L = 11;
    var R = 100;
    var d = 2;
    var K = 1;
    System.out.println ( solve ( R ) - solve ( L - 1 ) );
}
 