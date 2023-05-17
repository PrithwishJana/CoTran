public void System.out.printlnArray ( arr , n ) {
    for i in range ( n ) :
        System.out.println ( arr { i } , var end = " " ) ;;
}
public void removeMin ( arr , n ) {
    var minVal = arr { 0 } ;;
    for i in range ( 1 , n ) :
        minVal = min ( minVal , arr { i } ) ;;
    for i in range ( n ) :
        arr { i } = arr { i } - minVal ;;
}
public void removeFromMax ( arr , n ) {
    var maxVal = arr { 0 } ;;
    for i in range ( 1 , n ) :
        maxVal = max ( maxVal , arr { i } ) ;;
    for i in range ( n ) :
        arr { i } = maxVal - arr { i } ;;
}
public void modifyArray ( arr , n , k ) {
    if (( k % var 2 == 0 )) {
        removeMin ( arr , n ) ;;
    }
     else{
        removeFromMax ( arr , n ) ;;
    }
    System.out.printlnArray ( arr , n ) ;;
}
if (var __name__ == "__main__") {
    var arr = { 4 , 8 , 12 , 16 } ;;
    var n = len ( arr );
    var k = 2 ;;
    modifyArray ( arr , n , k ) ;;
}
 