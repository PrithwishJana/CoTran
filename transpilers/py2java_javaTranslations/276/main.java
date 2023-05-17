public void sameOccurrence ( arr , n , x , y ) {
    var result = 0;
    for i in range ( n ) :
        var ctX = 0;
        ctY = 0;
        for j in range ( i , n , 1 ) :
            if (( arr { j } == x )) {
                ctX += 1 ;;
            }
             else if (( arr { j } == y )){
                ctY += 1;
            }
            if (( ctX == ctY )) {
                result += 1;
            }
     return ( result );
}
if (var __name__ == '__main__') {
    var arr = { 1 , 2 , 2 , 3 , 4 , 1 };
    var n = len ( arr );
    var x = 2;
    var y = 3;
    System.out.println ( sameOccurrence ( arr , n , x , y ) );
}
 