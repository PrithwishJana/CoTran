var INF = 10 ** 10;
var MOD = 10 ** 9 + 7;
public void solve ( A , B , C ) {
    var A = A { : : - 1 };
    B = B { : : - 1 };
    C = C { : : - 1 };
    before = { 1 , 0 , 0 };
    N = len ( A );
    for i in range ( N ) :
        dp = { 0 } * 3;
        s = 0;
        if (i == N - 1) {
            s += 1;
        }
         for j in range ( 3 ) :
            for a in range ( s , 10 ) :
                if (A { i } != '?' and int ( A { i } ) != a) {
                    continue;
                }
                 for b in range ( s , 10 ) :
                    if (B { i } != '?' and int ( B { i } ) != b) {
                        continue;
                    }
                     for c in range ( s , 10 ) :
                        if (C { i } != '?' and int ( C { i } ) != c) {
                            continue;
                        }
                         if (( j + a + b ) % 10 != c) {
                            continue;
                        }
                         dp { ( j + a + b ) // 10 } += before { j };
                        dp { ( j + a + b ) // 10 } %= MOD;
        before = dp;
    ans = before { 0 };
    System.out.println ( ans );
}
public void main ( ) {
    while (true) {
        A = input ( );
        if (A == '0') {
            return;
        }
         var B = input ( );
        var C = input ( );
        solve ( A , B , C );
    }
 }
if (var __name__ == '__main__') {
    main ( );
}
 