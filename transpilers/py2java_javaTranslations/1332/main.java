public void findElements ( arr , n ) {
    for i in range ( n ) :
        var count = 0;
        for j in range ( 0 , n ) :
            if (arr { j } > arr { i }) {
                count = count + 1;
            }
         if (count >= 2) {
            System.out.println ( arr { i } , var end = " " );
        }
 }
var arr = { 2 , - 6 , 3 , 5 , 1 };
var n = len ( arr );
findElements ( arr , n );
