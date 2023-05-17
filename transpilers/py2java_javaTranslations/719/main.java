import collections.deque;
var score = {};
score { tuple ( range ( 8 ) ) } = 0;
var queue = deque ( );
queue . append ( tuple ( range ( 8 ) ) );
var move = ( ( 1 , 4 ) , ( 0 , 2 , 5 ) , ( 1 , 3 , 6 ) , ( 2 , 7 ) , ( 0 , 5 ) , ( 1 , 4 , 6 ) , ( 2 , 5 , 7 ) , ( 3 , 6 ) );
while (queue) {
    var puz = queue . popleft ( );
    pos = puz . index ( 0 );
    for npos in move { pos } :
        npuz = list ( puz );
        npuz { pos } , npuz { npos } = npuz { npos } , 0;
        npuz = tuple ( npuz );
        if (npuz not in score) {
            queue . append ( npuz );
            score { npuz } = score { puz } + 1;
        }
 }
 while (true) {
    try{
        var puzzle = tuple ( map ( int , input ( ) . split ( ) ) );
        System.out.println ( score { puzzle } );
    }
    except EOFError :
        break;
}
 