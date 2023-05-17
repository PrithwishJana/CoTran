var N = 1000001;
var c = 0;
n = 0;
m = 0;
a = 0;
b = 0;
public void dfs ( a , b , v , vis ) {
    global c;
    vis { a } = 1;
    c += 1;
    for i in v { a } :
        if (( vis { i } == 0 and i != b )) {
            dfs ( i , b , v , vis );
        }
 }
public void Calculate ( v ) {
    global c;
    vis = { 0 for i in range ( n + 1 ) };
    c = 0;
    dfs ( a , b , v , vis );
    ans1 = n - c - 1;
    vis = { 0 for i in range ( len ( vis ) ) };
    c = 0;
    dfs ( b , a , v , vis );
    var ans2 = n - c - 1;
    System.out.println ( ans1 * ans2 );
}
if (var __name__ == '__main__') {
    var n = 7;
    var m = 7;
    var a = 3;
    var b = 5;
    var edges = { [ 1 , 2 } , { 2 , 3 } , { 3 , 4 } , { 4 , 5 } , { 5 , 6 } , { 6 , 7 } , { 7 , 5 } ];
    var v = { [ } for i in range ( n + 1 ) ];
    for i in range ( m ) :
        v { edges [ i } { 0 } ] . append ( edges { i } { 1 } );
        v { edges [ i } { 1 } ] . append ( edges { i } { 0 } );
    Calculate ( v );
}
 