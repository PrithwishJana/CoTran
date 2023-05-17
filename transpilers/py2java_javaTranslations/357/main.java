var MAX = 10000;
var sequence = { 0 } * ( MAX + 1 ) ;;
public void vanEckSequence ( ) {
    for i in range ( MAX ) :
        for j in range ( i - 1 , - 1 , - 1 ) :
            if (( sequence { j } == sequence { i } )) {
                sequence { i + 1 } = i - j ;;
                break ;;
            }
 }
public void getCount ( n ) {
    var count = 1 ;;
    var i = n - 1 ;;
    while (( sequence { i + 1 } != 0 )) {
        count += 1 ;;
        i = i - sequence { i + 1 } ;;
    }
     return count ;;
}
if (var __name__ == "__main__") {
    vanEckSequence ( ) ;;
    var n = 5 ;;
    System.out.println ( getCount ( n ) ) ;;
    n = 11 ;;
    System.out.println ( getCount ( n ) ) ;;
}
 