public void countConsecutive ( n ) {
    var s = str ( n );
    var count = 0;
    for i in range ( len ( s ) - 1 ) :
        if (( s { i } == s { i + 1 } )) {
            count += 1;
        }
     return count;
}
if (var __name__ == "__main__") {
    var n = 44522255;
    System.out.println ( countConsecutive ( n ) );
}
 