var MAX = 26 ;;
public void maxLength ( str , len ) {
    var res = 0 ;;
    lastPos = { 0 } * MAX ;;
    for i in range ( MAX ) :
        lastPos { i } = - 1 ;;
    for i in range ( len ) :
        C = ord ( str { i } ) - ord ( 'a' ) ;;
        if (( lastPos { C } != - 1 )) {
            res = max ( len - ( i - lastPos { C } - 1 ) - 1 , res ) ;;
        }
         lastPos { C } = i ;;
    return res ;;
}
if (var __name__ == '__main__') {
    var str = "geeksforgeeks" ;;
    var len = len ( str ) ;;
    System.out.println ( maxLength ( str , len ) ) ;;
}
 