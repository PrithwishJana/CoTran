public void fact ( num ) {
    var fact = 1 ;;
    while (( num > 1 )) {
        fact = fact * num ;;
        var num = num - 1 ;;
    }
     return fact ;;
}
public void catalan ( n ) {
    return fact ( 2 * n ) // ( fact ( n ) * fact ( n + 1 ) );
}
if (var __name__ == '__main__') {
    var n = 5;
    var arr = { 1 , 2 , 3 , 4 , 5 };
    for k in range ( n ) :
        var s = 0;
        for i in range ( n ) :
            if (arr { i } < arr { k }) {
                s += 1;
            }
         var catalan_leftBST = catalan ( s );
        var catalan_rightBST = catalan ( n - s - 1 );
        var totalBST = catalan_rightBST * catalan_leftBST;
        System.out.println ( totalBST , var end = " " );
}
 