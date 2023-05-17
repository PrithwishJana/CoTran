import sys;
public void maxLength ( s , n ) {
    var ans = - ( sys . maxsize + 1 ) ;;
    A , L , R = {} , {} , {} ;;
    freq = { 0 } * ( n + 5 ) ;;
    for i in range ( 26 ) :
        count = 0 ;;
        for j in range ( n ) :
            if (( ord ( s { j } ) - ord ( 'a' ) == i )) {
                count += 1 ;;
            }
             freq { j } = count ;;
        for j in range ( n ) :
            L . append ( ( 2 * freq { j - 1 } ) - j ) ;;
            R . append ( ( 2 * freq { j } ) - j ) ;;
        max_len = - ( sys . maxsize + 1 ) ;;
        min_val = sys . maxsize ;;
        for j in range ( n ) :
            min_val = min ( min_val , L { j } ) ;;
            A . append ( min_val ) ;;
            l = 0 ; r = j ;;
            while (( l <= r )) {
                mid = ( l + r ) >> 1 ;;
                if (( A { mid } <= R { j } )) {
                    max_len = max ( max_len , j - mid + 1 ) ;;
                    r = mid - 1 ;;
                }
                 else{
                    l = mid + 1 ;;
                }
            }
         ans = max ( ans , max_len ) ;;
        A . clear ( ) ;;
        R . clear ( ) ;;
        L . clear ( ) ;;
    return ans ;;
}
if (var __name__ == "__main__") {
    var s = "ababbbacbcbcca" ;;
    var n = len ( s ) ;;
    System.out.println ( maxLength ( s , n ) ) ;;
}
 