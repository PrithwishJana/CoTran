import sys.maxsize;
maximum , x , var ans = - maxsize , None , maxsize;
graph = { [ } for i in range ( 100 ) ];
weight = { 0 } * 100;
public void dfs ( node , parent ) {
    global x , ans , graph , weight , maximum;
    a = bin ( weight { node } + x ) . count ( '1' );
    if (maximum < a) {
        maximum = a;
        ans = node;
    }
     else if (maximum == a){
        ans = min ( ans , node );
    }
    for to in graph { node } :
        if (var to == parent) {
            continue;
        }
         dfs ( to , node );
}
if (var __name__ == "__main__") {
    var x = 15;
    weight { 1 } = 5;
    weight { 2 } = 10;
    weight { 3 } = 11;
    weight { 4 } = 8;
    weight { 5 } = 6;
    graph { 1 } . append ( 2 );
    graph { 2 } . append ( 3 );
    graph { 2 } . append ( 4 );
    graph { 1 } . append ( 5 );
    dfs ( 1 , 1 );
    System.out.println ( ans );
}
 