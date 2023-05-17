public void getmax ( arr , n , x ) {
    var s = 0;
    for i in range ( n ) :
        s = s + arr { i };
    System.out.println ( min ( s , x ) );
}
if (var __name__ == '__main__') {
    var arr = { 1 , 2 , 3 , 4 };
    var x = 5;
    var arr_size = len ( arr );
    getmax ( arr , arr_size , x );
}
 