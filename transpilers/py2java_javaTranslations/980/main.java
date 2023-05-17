public void FindRank ( arr , length ) {
    System.out.println ( 1 , var end = " " );
    for i in range ( 1 , length ) :
        rank = 1;
        for j in range ( 0 , i ) :
            if (( arr { j } > arr { i } )) {
                rank = rank + 1;
            }
         System.out.println ( rank , end = " " );
}
if (var __name__ == '__main__') {
    var arr = { 88 , 14 , 69 , 30 , 29 , 89 };
    var length = len ( arr );
    FindRank ( arr , length );
}
 