public void maxAbsDiff ( arr , n ) {
    var minEle = arr { 0 };
    maxEle = arr { 0 };
    for i in range ( 1 , n ) :
        minEle = min ( minEle , arr { i } );
        var maxEle = max ( maxEle , arr { i } );
    return ( maxEle - minEle );
}
var arr = { 2 , 1 , 5 , 3 };
var n = len ( arr );
System.out.println ( maxAbsDiff ( arr , n ) );
