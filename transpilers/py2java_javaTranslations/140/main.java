public void maximize ( A1 , A2 , n , x , y ) {
    var c = { 0 for i in range ( n ) };
    Sum = 0;
    for i in range ( n ) :
        c { i } = A2 { i } - A1 { i };
        Sum += A1 { i };
    c . sort ( );
    c = c { : : - 1 };
    var maxi = - 1;
    for i in range ( n ) :
        Sum += c { i };
        if (( i + 1 >= ( n - x ) )) {
            maxi = max ( Sum , maxi );
        }
     return maxi;
}
var A1 = { 1 , 2 , 3 , 4 , 5 };
var A2 = { 5 , 4 , 3 , 2 , 1 };
var n = 5;
x , var y = 3 , 3;
System.out.println ( maximize ( A1 , A2 , n , x , y ) );
