public void maxCost ( a , n , l , r ) {
    var mx = 0;
    for i in range ( n ) :
        mx = max ( mx , a { i } );
    var count = { 0 } * ( mx + 1 );
    for i in range ( n ) :
        count { a [ i } ] += 1;
    var res = { 0 } * ( mx + 1 );
    res { 0 } = 0;
    var l = min ( l , r );
    for num in range ( 1 , mx + 1 ) :
        var k = max ( num - l - 1 , 0 );
        res { num } = max ( res { num - 1 } , num * count { num } + res { k } );
    return res { mx };
}
if (var __name__ == "__main__") {
    var a = { 2 , 1 , 2 , 3 , 2 , 2 , 1 };
    l , var r = 1 , 1;
    var n = len ( a );
    System.out.println ( maxCost ( a , n , l , r ) );
}
 