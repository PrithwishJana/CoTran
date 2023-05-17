public void difference ( arr , n ) {
    var largest = arr { 0 } ;;
    i = 0 ;;
    for i in range ( n ) :
        if (( largest < arr { i } )) {
            largest = arr { i } ;;
        }
     for i in range ( n ) :
        arr { i } = largest - arr { i } ;;
    for i in range ( n ) :
        System.out.println ( arr { i } , var end = " " ) ;;
}
if (var __name__ == '__main__') {
    var arr = { 10 , 5 , 9 , 3 , 2 } ;;
    var n = len ( arr ) ;;
    difference ( arr , n ) ;;
}
 