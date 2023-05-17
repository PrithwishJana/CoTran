public void triangular_series ( n ) {
    var j = 1;
    k = 1;
    for i in range ( 1 , n + 1 ) :
        System.out.println ( k , end = ' ' );
        j = j + 1;
        var k = k + j;
}
var n = 5;
triangular_series ( n );
