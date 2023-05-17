var N = 100;
public void ansQueries ( prefeven , prefodd , l , r ) {
    if (( ( r - l + 1 ) % var 2 == 0 )) {
        System.out.println ( "0" );
    }
     else{
        if (( l % 2 == 0 )) {
            System.out.println ( prefeven { r } ^ prefeven { l - 1 } );
        }
         else{
            System.out.println ( prefodd { r } ^ prefodd { l - 1 } );
        }
    }
}
public void wrapper ( arr , n , l , r , q ) {
    prefodd = { 0 } * N;
    prefeven = { 0 } * N;
    for i in range ( 1 , n + 1 ) :
        if (( ( i ) % 2 == 0 )) {
            prefeven { i } = arr { i - 1 } ^ prefeven { i - 1 };
            prefodd { i } = prefodd { i - 1 };
        }
         else{
            prefeven { i } = prefeven { i - 1 };
            prefodd { i } = prefodd { i - 1 } ^ arr { i - 1 };
        }
    var i = 0;
    while (( i != q )) {
        ansQueries ( prefeven , prefodd , l { i } , r { i } );
        i += 1;
    }
 }
if (var __name__ == "__main__") {
    var arr = { 1 , 2 , 3 , 4 , 5 };
    var n = len ( arr );
    var l = { 1 , 1 , 2 };
    var r = { 2 , 3 , 4 };
    var q = len ( l );
    wrapper ( arr , n , l , r , q );
}
 