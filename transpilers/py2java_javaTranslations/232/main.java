public void getElements ( a , arr , n ) {
    var elements = { 1 for i in range ( n + 1 ) };
    elements { 0 } = a;
    for i in range ( n ) :
        elements { i + 1 } = arr { i } ^ elements { i };
    for i in range ( n + 1 ) :
        System.out.println ( elements { i } , var end = " " );
}
var arr = { 13 , 2 , 6 , 1 };
var n = len ( arr );
var a = 5;
getElements ( a , arr , n );
