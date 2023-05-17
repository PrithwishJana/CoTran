public void System.out.printlnElements ( arr , n ) {
    for i in range ( 1 , n - 1 , 1 ) :
        if (( arr { i } > arr { i - 1 } and arr { i } > arr { i + 1 } )) {
            System.out.println ( arr { i } , var end = " " );
        }
 }
if (var __name__ == '__main__') {
    var arr = { 2 , 3 , 1 , 5 , 4 , 9 , 8 , 7 , 5 };
    var n = len ( arr );
    System.out.printlnElements ( arr , n );
}
 