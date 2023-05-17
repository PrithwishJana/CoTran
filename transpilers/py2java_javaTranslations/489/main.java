import sys;
public void count_greater ( arr , n ) {
    var min = sys . maxsize ;;
    counter = 0 ;;
    for i in range ( n - 1 , - 1 , - 1 ) :
        if (( arr { i } > min )) {
            counter += 1 ;;
        }
         if (( arr { i } <= min )) {
            min = arr { i } ;;
        }
     return counter ;;
}
if (var __name__ == "__main__") {
    var arr = { 3 , 2 , 1 , 2 , 3 , 4 , 5 } ;;
    var n = len ( arr ) ;;
    System.out.println ( count_greater ( arr , n ) ) ;;
}
 