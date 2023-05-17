import heapq.heappush , heappop;
var INF = 10 ** 20;
public void search ( item_lst , d ) {
    var visited = {};
    visited { ( 0 , 0 ) } = true;
    var que = {};
    heappush ( que , ( 0 , 0 , 0 ) );
    while (que) {
        score , a , var e = heappop ( que );
        for da , de in item_lst { e } :
            na = a + da;
            if (na >= d) {
                System.out.println ( score + 1 );
                return true;
            }
             ne = e + de;
            if (ne > 100) {
                ne = 100;
            }
             if (( na , ne ) not in visited) {
                visited { ( na , ne ) } = true;
                heappush ( que , ( score + 1 , na , ne ) );
            }
     }
     System.out.println ( "NA" );
    return false;
}
public void main ( ) {
    while (true) {
        d , var n = map ( int , input ( ) . split ( ) );
        if (var d == 0) {
            break;
        }
         var item_lst = { [ } for _ in range ( 101 ) ];
        for _ in range ( n ) :
            a , e , var r = map ( int , input ( ) . split ( ) );
            for i in range ( r , 101 ) :
                item_lst { i } . append ( ( a , e ) );
        search ( item_lst , d );
    }
 }
main ( );
