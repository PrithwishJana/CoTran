import sys;
var R = 4;
var C = 4;
public void first ( arr , low , high ) {
    if (( high >= low )) {
        var mid = low + ( high - low ) // 2 ;;
        if (( ( mid == 0 or arr { mid - 1 } == 0 ) and arr { mid } == 1 )) {
            return mid ;;
        }
         else if (( arr { mid } == 0 )){
            return first ( arr , ( mid + 1 ) , high ) ;;
        }
        else{
            return first ( arr , low , ( mid - 1 ) ) ;;
        }
    }
     return - 1 ;;
}
public void rowWith0s ( mat ) {
    var row_index = 0 ; max = - ( sys . maxsize - 1 ) ;;
    min_row_index = 0 ; min = sys . maxsize ;;
    for i in range ( R ) :
        index = first ( mat { i } , 0 , C - 1 ) ;;
        cntZeroes = 0 ;;
        if (( index == - 1 )) {
            cntZeroes = C ;;
        }
         else{
            cntZeroes = index ;;
        }
        if (( max < cntZeroes )) {
            max = cntZeroes ;;
            max_row_index = i ;;
        }
         if (( min > cntZeroes )) {
            min = cntZeroes ;;
            min_row_index = i ;;
        }
     System.out.println ( "Row with min 0s:" , min_row_index + 1 ) ;;
    System.out.println ( "Row with max 0s:" , max_row_index + 1 ) ;;
}
if (var __name__ == "__main__") {
    var mat = { [ 0 , 0 , 0 , 1 } , { 0 , 1 , 1 , 1 } , { 1 , 1 , 1 , 1 } , { 0 , 0 , 0 , 0 } ] ;;
    rowWith0s ( mat ) ;;
}
 