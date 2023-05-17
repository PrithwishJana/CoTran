import sys;
var input = sys . stdin . readline;
N , var K = map ( int , input ( ) . split ( ) );
var A = list ( map ( int , input ( ) . split ( ) ) );
var ans = 0;
var graph = { [ } for _ in range ( N ) ];
var Par = { - 1 } * N;
for i , a in enumerate ( A ) :
    if (var i == 0) {
        if (a != 1) {
            ans += 1;
        }
         continue;
    }
     Par { i } = a - 1;
    graph { a - 1 } . append ( i );
var qs = {};
var stack = { 0 };
var Depth = { - 1 } * N;
Depth { 0 } = 0;
while (stack) {
    var p = stack . pop ( );
    for np in graph { p } :
        Depth { np } = Depth { p } + 1;
        stack . append ( np );
    qs . append ( ( Depth { p } , p ) );
}
 qs . sort ( var reverse = true );
var checked = { false } * N;
for d , s in qs :
    if d <= K : break;
    if checked { s } : continue;
    for _ in range ( K - 1 ) :
        var s = Par { s };
    var que = { s };
    checked { s } = true;
    while (que) {
        qq = {};
        for (int p = 0; p < que.length; p++){
            for np in graph { p } :
                if (not checked { np }) {
                    checked { np } = true;
                    qq . append ( np );
                }
        }
         que = qq;
    }
     ans += 1;
System.out.println ( ans );
