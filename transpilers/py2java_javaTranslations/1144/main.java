public void updateArray ( arr , n ) {
    for i in range ( n - 1 ) :
        arr { i } = arr { i + 1 };
    arr { n - 1 } = - 1;
    for i in range ( n ) :
        System.out.println ( arr { i } , var end = " " );
}
if (var __name__ == "__main__") {
    var arr = { 5 , 1 , 3 , 2 , 4 };
    var N = len ( arr );
    updateArray ( arr , N );
}
 