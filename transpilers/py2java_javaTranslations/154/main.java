import collections.defaultdict;
var n = int ( input ( ) );
var graph = defaultdict ( list );
for _ in range ( n - 1 ) :
    i , var j = { int ( x ) for x in input ( ) . split ( ) };
    graph { i } . append ( j );
    graph { j } . append ( i );
var left = 0;
var right = 0;
var color = defaultdict ( int );
var visited = set ( );
public void dfs ( node ) {
    var level = { node };
    if (node not in color) {
        color { node } = 1;
    }
     while (level) {
        var node = level . pop ( );
        for val in graph { node } :
            if (val not in visited) {
                color { val } = 1 - color { node };
                visited . add ( val );
                level . append ( val );
            }
     }
 }
for i in range ( 1 , n + 1 ) :
    if (i not in visited) {
        visited . add ( i );
        dfs ( i );
    }
 for val in range ( 1 , n + 1 ) :
    if (color { val } == 0) {
        left += 1;
    }
     else{
        right += 1;
    }
System.out.println ( left * right - n + 1 );
