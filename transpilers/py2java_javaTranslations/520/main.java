public void countOddNumber ( row_num ) {
    var count = 0;
    while (row_num != 0) {
        count += row_num & 1;
        row_num >>= 1;
    }
     return ( 1 << count );
}
public void gouldSequence ( n ) {
    for row_num in range ( 0 , n ) :
        System.out.println ( countOddNumber ( row_num ) , var end = " " );
}
if (var __name__ == "__main__") {
    var n = 16;
    gouldSequence ( n );
}
 