import sys;
public void checkIfSortRotated ( arr , n ) {
    var minEle = sys . maxsize;
    maxEle = - sys . maxsize - 1;
    minIndex = - 1;
    for i in range ( n ) :
        if (arr { i } < minEle) {
            minEle = arr { i };
            var minIndex = i;
        }
     var flag1 = 1;
    for i in range ( 1 , minIndex ) :
        if (arr { i } < arr { i - 1 }) {
            flag1 = 0;
            break;
        }
     var flag2 = 2;
    for i in range ( minIndex + 1 , n ) :
        if (arr { i } < arr { i - 1 }) {
            flag2 = 0;
            break;
        }
     if (( flag1 and flag2 and arr { n - 1 } < arr { minIndex - 1 } )) {
        System.out.println ( "YES" );
    }
     else{
        System.out.println ( "NO" );
    }
}
var arr = { 3 , 4 , 5 , 1 , 2 };
var n = len ( arr );
checkIfSortRotated ( arr , n );
