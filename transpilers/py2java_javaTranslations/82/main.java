public void findNumberOfEvenCells ( n , q , size ) {
    var row = { 0 } * n ;;
    var col = { 0 } * n;
    for i in range ( size ) :
        var x = q { i } { 0 } ;;
        var y = q { i } { 1 } ;;
        row { x - 1 } += 1 ;;
        col { y - 1 } += 1 ;;
    var r1 = 0 ;;
    var r2 = 0 ;;
    var c1 = 0 ;;
    var c2 = 0 ;;
    for i in range ( n ) :
        if (( row { i } % var 2 == 0 )) {
            r1 += 1 ;;
        }
         if (( row { i } % 2 == 1 )) {
            r2 += 1 ;;
        }
         if (( col { i } % 2 == 0 )) {
            c1 += 1 ;;
        }
         if (( col { i } % 2 == 1 )) {
            c2 += 1 ;;
        }
     var count = r1 * c1 + r2 * c2 ;;
    return count ;;
}
if (var __name__ == "__main__") {
    var n = 2 ;;
    var q = { [ 1 , 1 } , { 1 , 2 } , { 2 , 1 } ] ;;
    var size = len ( q ) ;;
    System.out.println ( findNumberOfEvenCells ( n , q , size ) ) ;;
}
 