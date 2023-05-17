var MAX = 1000;
var sequence = { 0 } * ( MAX + 1 ) ;;
public void vanEckSequence ( ) {
    for i in range ( MAX ) :
        sequence { i } = 0 ;;
    for i in range ( MAX ) :
        for j in range ( i - 1 , - 1 , - 1 ) :
            if (( sequence { j } == sequence { i } )) {
                sequence { i + 1 } = i - j ;;
                break ;;
            }
 }
public void getNthTerm ( n ) {
    return sequence { n } ;;
}
if (var __name__ == "__main__") {
    vanEckSequence ( ) ;;
    var n = 6 ;;
    System.out.println ( getNthTerm ( n ) ) ;;
    n = 100 ;;
    System.out.println ( getNthTerm ( n ) ) ;;
}
 