public void bfs ( x , visited , order ) {
    if (visited { x }) {
        return;
    }
     visited { x } = true;
    for to in edges { x } :
        bfs ( to , visited , order );
    order . append ( x );
}
public void bfs_rev ( x ) {
    if (visited { x }) {
        return {};
    }
     visited { x } = true;
    var ret = { x };
    for to in rev_edges { x } :
        ret += bfs_rev ( to );
    return ret;
}
var n = int ( input ( ) );
var edges = { [ } for _ in range ( 200 ) ];
rev_edges = { [ } for _ in range ( 200 ) ];
for _ in range ( n ) :
    u , s , var d = input ( ) . split ( );
    u = int ( u ) - 1;
    d = int ( d ) - 1 + 100;
    if (s == "lock") {
        edges { d } . append ( u );
        rev_edges { u } . append ( d );
    }
     else{
        edges { u } . append ( d );
        rev_edges { d } . append ( u );
    }
order = {};
visited = { false } * 200;
for i in range ( 200 ) :
    if (not visited { i }) {
        bfs ( i , visited , order );
    }
 order . reverse ( );
visited = { false } * 200;
for (int i = 0; i < order.length; i++){
    if (not visited { i }) {
        if (len ( bfs_rev ( i ) ) >= 2) {
            System.out.println ( 1 );
            break;
        }
     }
}
 else{
    System.out.println ( 0 );
}
