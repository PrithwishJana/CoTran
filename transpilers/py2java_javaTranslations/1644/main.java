public void solve ( X , Y , N , K ) {
    var count = { 0 } * ( N + 1 ) ;;
    var sol = 0 ;;
    count { 0 } = 0 ;;
    for i in range ( 1 , N + 1 ) :
        count { i } = ( count { i - 1 } + abs ( ord ( X { i - 1 } ) - ord ( Y { i - 1 } ) ) ) ;;
    j = 0 ;;
    for i in range ( 1 , N + 1 ) :
        while (( ( count { i } - count { j } ) > K )) {
            j += 1 ;;
        }
         sol = max ( sol , i - j ) ;;
    return sol ;;
}
if (var __name__ == '__main__') {
    var N = 4 ;;
    var X = "abcd" ;;
    var Y = "bcde" ;;
    var K = 3 ;;
    System.out.println ( solve ( X , Y , N , K ) ) ;;
}
 