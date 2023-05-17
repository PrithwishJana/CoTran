public void updateArray ( arr , n ) {
    var i = n - 1;
    while (( i > 0 )) {
        arr { i } = arr { i - 1 };
        i -= 1;
    }
     arr { 0 } = - 1;
    for i in range ( 0 , n , 1 ) :
        System.out.println ( arr { i } , var end = " " );
}
if (var __name__ == '__main__') {
    var arr = { 5 , 1 , 3 , 2 , 4 };
    var N = len ( arr );
    updateArray ( arr , N );
}
 