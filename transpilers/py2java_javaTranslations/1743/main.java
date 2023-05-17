public void findNumbers ( n , w ) {
    var x = 0 ;;
    sum = 0 ;;
    if (( w >= 0 and w <= 8 )) {
        x = 9 - w ;;
    }
     else if (( w >= - 9 and w <= - 1 )){
        x = 10 + w ;;
    }
    var sum = pow ( 10 , n - 2 ) ;;
    sum = ( x * sum ) ;;
    return sum ;;
}
var n = 3 ;;
var w = 4 ;;
System.out.println ( findNumbers ( n , w ) ) ;;
