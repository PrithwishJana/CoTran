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
    var nthTerm = sequence { n - 1 } ;;
    var count = 0 ;;
    for i in range ( n ) :
        if (( sequence { i } == nthTerm )) {
            count += 1 ;;
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
 