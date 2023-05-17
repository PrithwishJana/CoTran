import sys ;;
public void FindSubarray ( arr , n , k ) {
    var count_one = { 0 } * n ;;
    for i in range ( n ) :
        count_one { i } = bin ( arr { i } ) . count ( '1' ) ;;
    var sum = count_one { 0 } ;;
    if (( var n == 1 )) {
        if (( count_one { 0 } >= k )) {
            return 1 ;;
        }
         else{
            return - 1 ;;
        }
    }
     ans = sys . maxsize ;;
    i = 1 ;;
    j = 0 ;;
    while (( i < n )) {
        if (( k == count_one { j } )) {
            ans = 1 ;;
            break ;;
        }
         else if (( k == count_one { i } )){
            ans = 1 ;;
            break ;;
        }
        else if (( sum + count_one { i } < k )){
            sum += count_one { i } ;;
            i += 1 ;;
        }
        else if (( sum + count_one { i } > k )){
            ans = min ( ans , ( i - j ) + 1 ) ;;
            sum -= count_one { j } ;;
            j += 1 ;;
        }
        else if (( sum + count_one { i } == k )){
            ans = min ( ans , ( i - j ) + 1 ) ;;
            sum += count_one { i } ;;
            i += 1 ;;
        }
    }
     if (( ans != sys . maxsize )) {
        return ans ;;
     }
     else{
        return - 1 ;;
    }
}
if (__name__ == "__main__") {
    arr = { 1 , 2 , 4 , 8 } ;;
    n = len ( arr ) ;;
    var k = 2 ;;
    System.out.println ( FindSubarray ( arr , n , k ) ) ;;
}
 