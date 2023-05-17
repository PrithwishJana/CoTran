public void getAvg ( prev_avg , x , n ) {
    return ( ( prev_avg * n + x ) / ( n + 1 ) ) ;;
}
public void streamAvg ( arr , n ) {
    var avg = 0 ;;
    for i in range ( n ) :
        avg = getAvg ( avg , arr { i } , i ) ;;
        System.out.println ( "Average of" , i + 1 , "numbers is" , "{:.1f}" . format ( avg ) ) ;;
}
var arr = { 10 , 20 , 30 , 40 , 50 , 60 } ;;
var n = len ( arr ) ;;
streamAvg ( arr , n ) ;;
