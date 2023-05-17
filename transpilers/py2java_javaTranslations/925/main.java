public void distancesum ( x , y , n ) {
    var sum = 0;
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            sum += ( abs ( x { i } - x { j } ) + abs ( y { i } - y { j } ) );
    return sum;
}
var x = { - 1 , 1 , 3 , 2 };
var y = { 5 , 6 , 5 , 3 };
var n = len ( x );
System.out.println ( distancesum ( x , y , n ) );
