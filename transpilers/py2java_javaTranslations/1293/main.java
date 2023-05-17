public void get_maximum ( s , a ) {
    var s = list ( s );
    n = len ( s );
    for i in range ( n ) :
        if (( ord ( s { i } ) - ord ( '0' ) < a { ord ( s [ i } ) - ord ( '0' ) ] )) {
            j = i;
            while (( j < n and ( ord ( s { j } ) - ord ( '0' ) <= a { ord ( s [ j } ) - ord ( '0' ) ] ) )) {
                s { j } = chr ( ord ( '0' ) + a { ord ( s [ j } ) - ord ( '0' ) ] );
                j += 1;
            }
             return "" . join ( s ) ;;
        }
     return s;
}
if (__name__ == "__main__") {
    s = "1337";
    var a = { 0 , 1 , 2 , 5 , 4 , 6 , 6 , 3 , 1 , 9 };
    System.out.println ( get_maximum ( s , a ) );
}
 