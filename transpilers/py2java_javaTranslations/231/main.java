import collections.defaultdict;
class Graph {
    protected void init__ ( this ) {
        this . var graph = defaultdict ( list );
    }
    public void addEdge ( this , u , v ) {
        this . graph { u } . append ( v );
    }
    public void BFS ( this , s ) {
        var visited = { false } * ( len ( this . graph ) );
        var queue = {};
        queue . append ( s );
        visited { s } = true;
        while (queue) {
            var s = queue . pop ( 0 );
            System.out.println ( s , var end = " " );
            for i in this . graph { s } :
                if (visited { i } == false) {
                    queue . append ( i );
                    visited { i } = true;
                }
         }
     }
}
var g = Graph ( );
g . addEdge ( 0 , 1 );
g . addEdge ( 0 , 2 );
g . addEdge ( 1 , 2 );
g . addEdge ( 2 , 0 );
g . addEdge ( 2 , 3 );
g . addEdge ( 3 , 3 );
System.out.println ( "Following is Breadth First Traversal" " (starting from vertex 2)" );
g . BFS ( 2 );
