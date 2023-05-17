public void find_longest ( node ) {
    global visited;
    visited { node } = true;
    if (node not in graph) {
        return 1;
    }
     var max_child = 0;
    for i in graph { node } :
        if (visited { i }) {
            continue;
        }
         max_child = max ( max_child , find_longest ( i ) );
    return max_child + 1;
}
public void dfs ( node ) {
    var vis = { 0 for i in range ( len ( FF ) ) };
    vis { node } = 1;
    var size = 1;
    var tmp = node;
    while (true) {
        tmp = FF { tmp };
        if (tmp == node) {
            return size;
        }
         if (vis { tmp } == 1) {
            return 0;
        }
         vis { tmp } = 1;
        size += 1;
    }
     return 0;
}
var visited = {};
graph = {};
Q = int ( input ( ) );
for q in range ( Q ) :
    N = int ( input ( ) );
    FF = list ( map ( int , input ( ) . split ( ) ) );
    FF . insert ( 0 , - 1 );
    graph = {};
    visited = { false for i in range ( N + 1 ) };
    for i in range ( 1 , len ( FF ) ) :
        if (FF { i } not in graph) {
            graph { FF [ i } ] = {};
        }
         graph { FF [ i } ] . append ( i );
    var double = 0;
    for i in range ( 1 , N + 1 ) :
        if (i == FF { FF [ i } ] and not visited { i }) {
            visited { i } = true;
            visited { FF [ i } ] = true;
            dou = find_longest ( i ) + find_longest ( FF { i } );
            double += dou;
        }
     for i in range ( 1 , N + 1 ) :
        if (not visited { i }) {
            double = max ( double , dfs ( i ) );
        }
     System.out.println ( "Case; //{}: {}" . format ( q + 1 , double ) )
