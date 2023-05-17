var MAX = 25 ;;
public void getMinSum ( arr , n ) {
    var bits_count = { 0 } * MAX;
    var max_bit = 0 ; sum = 0 ; ans = 0 ;;
    for d in range ( n ) :
        e = arr { d } ; f = 0 ;;
        while (( e > 0 )) {
            rem = e % 2 ;;
            e = e // 2 ;;
            if (( rem == 1 )) {
                bits_count { f } += rem ;;
            }
             f += 1;
        }
         max_bit = max ( max_bit , f ) ;;
    for d in range ( max_bit ) :
        var temp = pow ( 2 , d ) ;;
        if (( bits_count { d } > n // 2 )) {
            var ans = ans + temp ;;
        }
     for d in range ( n ) :
        arr { d } = arr { d } ^ ans ;;
        var sum = sum + arr { d } ;;
    return sum;
}
if (var __name__ == "__main__") {
    var arr = { 3 , 5 , 7 , 11 , 15 } ;;
    var n = len ( arr ) ;;
    System.out.println ( getMinSum ( arr , n ) );
}
 