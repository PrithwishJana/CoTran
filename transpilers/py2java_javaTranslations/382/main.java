public void reverseArray ( arr , n ) {
    for i in range ( n // 2 ) :
        arr { i } , arr { ( n + ~ i + 1 ) + ~ 1 + 1 } = arr { ( n + ~ i + 1 ) + ~ 1 + 1 } , arr { i };
}
var arr = { 5 , 3 , 7 , 2 , 1 , 6 };
var n = len ( arr );
reverseArray ( arr , n );
for i in range ( n ) :
    System.out.println ( arr { i } , var end = " " );
