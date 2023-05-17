import math;
public void minInsertions ( H , n , K ) {
    var inser = 0 ;;
    for i in range ( 1 , n ) :
        var diff = abs ( H { i } - H { i - 1 } ) ;;
        if (( diff <= K )) {
            continue ;;
        }
         else{
            inser += math . ceil ( diff / K ) - 1 ;;
        }
    return inser ;;
}
var H = { 2 , 4 , 8 , 16 } ;;
var K = 3 ;;
var n = len ( H ) ;;
System.out.println ( minInsertions ( H , n , K ) ) ;;
