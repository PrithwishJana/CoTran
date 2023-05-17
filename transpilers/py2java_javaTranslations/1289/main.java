public void MinStep ( a , n ) {
    var positive = 0 ;;
    var negative = 0 ;;
    var zero = 0 ;;
    var step = 0 ;;
    for i in range ( n ) :
        if (( a { i } == 0 )) {
            zero += 1 ;;
        }
         else if (( a { i } < 0 )){
            negative += 1 ;;
            step = step + ( - 1 - a { i } ) ;;
        }
        else{
            positive += 1 ;;
            step = step + ( a { i } - 1 ) ;;
        }
    if (( negative % 2 == 0 )) {
        step = step + zero ;;
    }
     else{
        if (( zero > 0 )) {
            step = step + zero ;;
        }
         else{
            step = step + 2 ;;
        }
    }
    return step ;;
}
if (var __name__ == '__main__') {
    var a = { 0 , - 2 , - 1 , - 3 , 4 } ;;
    var n = len ( a ) ;;
    System.out.println ( MinStep ( a , n ) ) ;;
}
 