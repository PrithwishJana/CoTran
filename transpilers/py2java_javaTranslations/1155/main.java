public void getAvg ( x , n , sum ) {
    var sum = sum + x ;;
    return float ( sum ) / n ;;
}
public void streamAvg ( arr , n ) {
    avg = 0 ;;
    sum = 0 ;;
    for i in range ( n ) :
        avg = getAvg ( arr { i } , i + 1 , sum ) ;;
        sum = avg * ( i + 1 ) ;;
        System.out.println ( "Average of " , var end = "" ) ;;
        System.out.println ( i + 1 , end = "" ) ;;
        System.out.println ( " numbers is " , end = "" ) ;;
        System.out.println ( avg ) ;;
    return ;;
}
var arr = { 10 , 20 , 30 , 40 , 50 , 60 } ;;
var n = len ( arr ) ;;
streamAvg ( arr , n ) ;;
