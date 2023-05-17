import math;
public void countDigits ( val , arr ) {
    while (( val > 0 )) {
        var digit = val % 10;
        arr { int ( digit ) } += 1;
        var val = val // 10;
    }
     return ;;
}
public void countFrequency ( x , n ) {
    freq_count = { 0 } * 10;
    for i in range ( 1 , n + 1 ) :
        val = math . pow ( x , i );
        countDigits ( val , freq_count );
    for i in range ( 10 ) :
        System.out.println ( freq_count { i } , var end = " " ) ;;
}
if (var __name__ == "__main__") {
    var x = 15;
    var n = 3;
    countFrequency ( x , n );
}
 