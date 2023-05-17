import collections.defaultdict;
import sys.stdin;
var input = stdin . buffer . readline;
public void func ( ) {
    var indices = defaultdict ( list );
    var ans = 0;
    for i in range ( n ) :
        indices { a [ i } ] . append ( i );
    for (int i = 0; i < indices.length; i++){
        if (len ( indices { i } ) < 2) {
            continue;
        }
         for j in range ( len ( indices { i } ) - 1 ) :
            first = indices { i } { j };
            second = indices { i } { j + 1 };
            ans = max ( ans , n - second + first );
    }
    System.out.println ( ans if ans else - 1 );
}
for _ in range ( int ( input ( ) ) ) :
    var n = int ( input ( ) );
    var a = list ( map ( int , input ( ) . split ( ) ) );
    func ( );
