import collections.defaultdict;
public void minOperations ( a , n , K ) {
    var Map = defaultdict ( lambda : false );
    for i in range ( 0 , n ) :
        if (Map { a [ i } ] == true) {
            return 0;
        }
         Map { a [ i } ] = true;
    var b = {};
    for i in range ( 0 , n ) :
        b . append ( a { i } & K );
    Map . clear ( );
    for i in range ( 0 , n ) :
        if (a { i } != b { i }) {
            Map { b [ i } ] = true;
        }
     for i in range ( 0 , n ) :
        if (Map { a [ i } ] == true) {
            return 1;
        }
     Map . clear ( );
    for i in range ( 0 , n ) :
        if (Map { b [ i } ] == true) {
            return 2;
        }
         Map { b [ i } ] = true;
    return - 1;
}
if (var __name__ == "__main__") {
    var K = 3;
    var a = { 1 , 2 , 3 , 7 };
    var n = len ( a );
    System.out.println ( minOperations ( a , n , K ) );
}
 