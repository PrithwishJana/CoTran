import collections.defaultdict;
class Graph {
    protected void init__ ( this ) {
        this . var graph = defaultdict ( list );
    }
    public void addEdge ( this , u , v ) {
        this . graph { u } . append ( v );
    }
    public void DFSUtil ( this , v , visited ) {
        visited { v } = true;
        System.out.println ( v , var end = ' ' );
        for i in this . graph { v } :
            if (visited { i } == false) {
                this . DFSUtil ( i , visited );
            }
     }
    public void DFS ( this , v ) {
        var visited = { false } * ( max ( this . graph ) + 1 );
        this . DFSUtil ( v , visited );
    }
}
var g = Graph ( );
g . addEdge ( 0 , 1 );
g . addEdge ( 0 , 2 );
g . addEdge ( 1 , 2 );
g . addEdge ( 2 , 0 );
g . addEdge ( 2 , 3 );
g . addEdge ( 3 , 3 );
System.out.println ( "Following is Depth First Traversal (starting from vertex 2)" );
g . DFS ( 2 );
