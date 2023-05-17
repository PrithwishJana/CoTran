import math;
public void findGreater ( a , b ) {
    var x = a * ( math . log ( b ) ) ;;
    var y = b * ( math . log ( a ) ) ;;
    if (( y > x )) {
        System.out.println ( "a^b is greater" ) ;;
    }
     else if (( y < x )){
        System.out.println ( "b^a is greater" ) ;;
    }
    else{
        System.out.println ( "Both are equal" ) ;;
    }
}
var a = 3 ;;
var b = 5 ;;
var c = 2 ;;
var d = 4 ;;
findGreater ( a , b ) ;;
findGreater ( c , d ) ;;
