public void originalArray ( greater , n ) {
    var temp = {};
    for i in range ( n + 1 ) :
        temp . append ( i );
    var arr = { 0 for i in range ( n ) };
    for i in range ( n ) :
        k = n - greater { i } - i;
        arr { i } = temp { k };
        del temp { k };
    for i in range ( n ) :
        System.out.println ( arr { i } , end = " " );
}
arr = { 6 , 3 , 2 , 1 , 0 , 1 , 0 };
var n = len ( arr );
originalArray ( arr , n );
