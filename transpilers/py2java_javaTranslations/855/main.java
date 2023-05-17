public void subString ( s , n ) {
    for i in range ( n ) :
        for len in range ( i + 1 , n + 1 ) :
            System.out.println ( s { i : len } ) ;;
}
var s = "abcd" ;;
subString ( s , len ( s ) ) ;;
