var mod = 1000000007;
var eps = 10 ** - 9;
public void main ( ) {
    import sys;
    import collections.deque;
    var input = sys . stdin . buffer . readline;
    N , var M = map ( int , input ( ) . split ( ) );
    var adj = { [ } for _ in range ( N + 1 ) ];
    for _ in range ( M ) :
        a , var b = map ( int , input ( ) . split ( ) );
        adj { a } . append ( b );
        adj { b } . append ( a );
    var seen = { 0 } * ( N + 1 );
    var single = 0;
    var bipartite = 0;
    not_bipartite = 0;
    for v0 in range ( 1 , N + 1 ) :
        if (seen { v0 } != 0) {
            continue;
        }
         var flg = 1;
        que = deque ( );
        que . append ( v0 );
        seen { v0 } = 1;
        cnt = 0;
        while (que) {
            v = que . popleft ( );
            cnt += 1;
            for u in adj { v } :
                if (seen { u } == 0) {
                    seen { u } = - seen { v };
                    que . append ( u );
                }
                 else{
                    if (seen { u } == seen { v }) {
                        flg = 0;
                    }
                 }
        }
         if (var cnt == 1) {
            single += 1;
         }
         else{
            if (flg) {
                bipartite += 1;
            }
             else{
                not_bipartite += 1;
            }
        }
    var ans = N ** 2 - ( N - single ) ** 2;
    ans += ( bipartite + not_bipartite ) ** 2;
    ans += bipartite ** 2;
    System.out.println ( ans );
}
if (var __name__ == '__main__') {
    main ( );
}
 