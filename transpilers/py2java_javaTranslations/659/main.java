public void maxSum ( arr , n ) {
    arr . sort ( );
    var sum = 0;
    for i in range ( n ) :
        sum += arr { i } * i;
    return sum;
}
var arr = { 3 , 5 , 6 , 1 };
var n = len ( arr );
System.out.println ( maxSum ( arr , n ) );
