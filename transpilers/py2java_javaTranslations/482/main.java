public void System.out.printlnPairs ( arr , n ) {
    var v = {};
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if (( abs ( arr { i } ) == abs ( arr { j } ) )) {
                v . append ( abs ( arr { i } ) );
            }
     if (( len ( v ) == 0 )) {
        return ;;
    }
     v . sort ( );
    for i in range ( len ( v ) ) :
        System.out.println ( - v { i } , v { i } , var end = " " );
}
if (var __name__ == "__main__") {
    var arr = { 4 , 8 , 9 , - 4 , 1 , - 1 , - 8 , - 9 };
    var n = len ( arr );
    System.out.printlnPairs ( arr , n );
}
 