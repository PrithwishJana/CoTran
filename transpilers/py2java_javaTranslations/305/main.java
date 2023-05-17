var N = 100005;
var gr = { [ } for i in range ( N ) ];
var colour = { - 1 } * N;
var edges = {};
var bip = true;
public void add_edge ( x , y ) {
    gr { x } . append ( y );
    gr { y } . append ( x );
    edges . append ( ( x , y ) );
}
public void dfs ( x , col ) {
    colour { x } = col;
    global bip;
    for i in gr { x } :
        if (colour { i } == - 1) {
            dfs ( i , col ^ 1 );
        }
         else if (colour { i } == col){
            bip = false;
        }
}
public void Directed_Graph ( n , m ) {
    dfs ( 1 , 1 );
    if (not bip) {
        System.out.println ( - 1 );
        return;
    }
     for i in range ( 0 , m ) :
        if (colour { edges [ i } { 0 } ] == 0) {
            edges { i } { 0 } , edges { i } { 1 } = edges { i } { 1 } , edges { i } { 0 };
        }
         System.out.println ( edges { i } { 0 } , edges { i } { 1 } );
}
if (var __name__ == "__main__") {
    n , var m = 4 , 3;
    add_edge ( 1 , 2 );
    add_edge ( 1 , 3 );
    add_edge ( 1 , 4 );
    Directed_Graph ( n , m );
}
 