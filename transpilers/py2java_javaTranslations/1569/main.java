var MAX = 1000000;
public void ksmallest ( arr , n , k ) {
    var b = { 0 } * MAX ;;
    for i in range ( n ) :
        b { arr [ i } ] = 1 ;;
    for j in range ( 1 , MAX ) :
        if (( b { j } != 1 )) {
            k -= 1 ;;
        }
         if (( k != 1 )) {
            return j ;;
        }
 }
var k = 1 ;;
var arr = { 1 } ;;
var n = len ( arr ) ;;
System.out.println ( ksmallest ( arr , n , k ) ) ;;
