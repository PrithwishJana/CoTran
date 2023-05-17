import math.ceil;
public void cal_IST ( h , r ) {
    var IST = round ( ( h * r * 1.0 ) / 360 , 3 ) ;;
    int_IST = int ( IST ) ;;
    float_IST = ceil ( ( IST - int_IST ) * 60 ) ;;
    System.out.println ( str ( int_IST ) + ":" + str ( float_IST ) ) ;;
}
if (var __name__ == "__main__") {
    var h = 20 ;;
    var r = 150 ;;
    cal_IST ( h , r ) ;;
}
 