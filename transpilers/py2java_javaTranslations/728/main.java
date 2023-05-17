import heapq;
n , var q = map ( int , input ( ) . split ( ) );
var Q = { [ } for i in range ( n ) ];
var queries = list ( );
for i in range ( q ) :
    queries . append ( list ( map ( int , input ( ) . split ( ) ) ) );
for (int query = 0; query < queries.length; query++){
    if (query { 0 } == 0) {
        heapq . heappush ( Q { query [ 1 } ] , - query { 2 } );
    }
     else if (query { 0 } == 1){
        if (Q { query [ 1 } ]) {
            System.out.println ( - Q { query [ 1 } ] { 0 } );
        }
     }
    else if (query { 0 } == 2){
        if (Q { query [ 1 } ]) {
            heapq . heappop ( Q { query [ 1 } ] );
        }
     }
}
