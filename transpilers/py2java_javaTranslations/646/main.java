public void zeroUpto ( digits ) {
    var first = int ( ( pow ( 10 , digits ) - 1 ) / 9 ) ;;
    var second = int ( ( pow ( 9 , digits ) - 1 ) / 8 ) ;;
    return 9 * ( first - second ) ;;
}
public void countZero ( num ) {
    var k = len ( num ) ;;
    var total = zeroUpto ( k - 1 ) ;;
    var non_zero = 0 ;;
    for i in range ( len ( num ) ) :
        if (( num { i } == '0' )) {
            non_zero -= 1 ;;
            break ;;
        }
         non_zero += ( ( ( ord ( num { i } ) - ord ( '0' ) ) - 1 ) * ( pow ( 9 , k - 1 - i ) ) ) ;;
    var no = 0 ;;
    remaining = 0 ;;
    calculatedUpto = 0 ;;
    for i in range ( len ( num ) ) :
        no = no * 10 + ( ord ( num { i } ) - ord ( '0' ) ) ;;
        if (( i != 0 )) {
            var calculatedUpto = calculatedUpto * 10 + 9 ;;
        }
     var remaining = no - calculatedUpto ;;
    var ans = zeroUpto ( k - 1 ) + ( remaining - non_zero - 1 ) ;;
    return ans ;;
}
var num = "107" ;;
System.out.println ( "Count of numbers from 1 to" , num , "is" , countZero ( num ) ) ;;
num = "1264" ;;
System.out.println ( "Count of numbers from 1 to" , num , "is" , countZero ( num ) ) ;;
