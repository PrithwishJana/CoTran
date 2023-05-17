public void System.out.printlnMax ( arr , n , k ) {
    var max = 0;
    for i in range ( n - k + 1 ) :
        max = arr { i };
        for j in range ( 1 , k ) :
            if (arr { i + j } > max) {
                max = arr { i + j };
            }
         System.out.println ( str ( max ) + " " , var end = "" );
}
if (var __name__ == "__main__") {
    var arr = { 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 };
    var n = len ( arr );
    var k = 3;
    System.out.printlnMax ( arr , n , k );
}
 