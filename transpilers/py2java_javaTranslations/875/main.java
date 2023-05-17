public void indexedSequentialSearch ( arr , n , k ) {
    var elements = { 0 } * 20;
    var indices = { 0 } * 20;
    j , var ind = 0 , 0;
    for i in range ( 0 , n , 3 ) :
        elements { ind } = arr { i };
        indices { ind } = i;
        ind += 1;
    if (k < elements { 0 }) {
        System.out.println ( "Not found" );
        exit ( 0 );
    }
     else{
        for i in range ( 1 , ind + 1 ) :
            if (k < elements { i }) {
                var start = indices { i - 1 };
                var end = indices { i };
                break;
            }
     }
    for i in range ( start , end + 1 ) :
        if (var k == arr { i }) {
            j = 1;
            break;
        }
     if (j == 1) {
        System.out.println ( "Found at index" , i );
    }
     else{
        System.out.println ( "Not found" );
    }
}
if (__name__ == "__main__") {
    arr = { 6 , 7 , 8 , 9 , 10 };
    n = len ( arr );
    k = 8;
    indexedSequentialSearch ( arr , n , k );
}
 