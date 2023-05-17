import sys;
public void getMinLength ( arr , n ) {
    var count = 0 ;;
    result = sys . maxsize ;;
    for i in range ( n ) :
        if (( arr { i } == 1 )) {
            count += 1 ;;
        }
         else{
            if (( count != 0 )) {
                result = min ( result , count ) ;;
            }
             count = 0 ;;
        }
    return result ;;
}
var arr = { 1 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 } ;;
var n = len ( arr ) ;;
System.out.println ( getMinLength ( arr , n ) ) ;;
