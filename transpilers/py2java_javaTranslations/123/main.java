var adjacency = { [ } for i in range ( 100 ) ];
public void insert ( x , y ) {
    adjacency { x } . append ( y );
}
public void dfs ( node , leaf , vis ) {
    leaf { node } = 0;
    vis { node } = 1;
    for it in adjacency { node } :
        if (( vis { it } == false )) {
            dfs ( it , leaf , vis );
            leaf { node } += leaf { it };
        }
     if (( len ( adjacency { node } ) == 0 )) {
        leaf { node } = 1;
    }
 }
public void System.out.printlnLeaf ( n , leaf ) {
    for i in range ( 1 , n + 1 ) :
        System.out.println ( "The node" , i , "has" , leaf { i } , "leaf nodes" );
}
var N = 6;
insert ( 1 , 2 );
insert ( 1 , 3 );
insert ( 3 , 4 );
insert ( 3 , 5 );
insert ( 3 , 6 );
var leaf = { 0 for i in range ( N + 1 ) };
var vis = { 0 for i in range ( N + 1 ) };
dfs ( 1 , leaf , vis );
System.out.printlnLeaf ( N , leaf );
