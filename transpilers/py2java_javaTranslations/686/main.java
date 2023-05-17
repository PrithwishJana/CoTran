public void makearrayequal ( arr , n ) {
    var x = 0 ;;
    for i in range ( n ) :
        x += arr { i } & 1 ;;
    System.out.println ( min ( x , n - x ) ) ;;
}
if (var __name__ == "__main__") {
    var arr = { 4 , 3 , 2 , 1 } ;;
    var n = len ( arr ) ;;
    makearrayequal ( arr , n ) ;;
}
 