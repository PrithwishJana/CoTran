public void colourVisible ( height , colour , K ) {
    var arr = { 0 for i in range ( K + 1 ) };
    var visible = 0;
    var max = height { K - 1 };
    arr { colour [ K - 1 } ] = 1;
    i = K - 2;
    while (( i >= 0 )) {
        if (( height { i } > max )) {
            max = height { i };
            arr { colour [ i } ] = 1;
        }
         i -= 1;
    }
     for i in range ( 1 , K + 1 , 1 ) :
        if (( arr { i } == 1 )) {
            visible += 1;
        }
     return visible;
}
if (var __name__ == '__main__') {
    var height = { 3 , 5 , 1 , 2 , 3 };
    var colour = { 1 , 2 , 3 , 4 , 3 };
    var K = len ( colour );
    System.out.println ( colourVisible ( height , colour , K ) );
}
 