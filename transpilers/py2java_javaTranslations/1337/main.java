import sys;
public void findMinDel ( arr , n ) {
    var min_num = sys . maxsize ;;
    for i in range ( n ) :
        min_num = min ( arr { i } , min_num ) ;;
    var cnt = 0 ;;
    for i in range ( n ) :
        if (( arr { i } == min_num )) {
            cnt += 1 ;;
        }
     return n - cnt ;;
}
if (var __name__ == "__main__") {
    var arr = { 3 , 3 , 2 } ;;
    var n = len ( arr ) ;;
    System.out.println ( findMinDel ( arr , n ) ) ;;
}
 