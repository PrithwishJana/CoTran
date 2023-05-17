public void findPairCount ( N , K ) {
    var count = 0 ;;
    var rem = { 0 } * K ;;
    rem { 0 } = N // K ;;
    for i in range ( 1 , K ) :
        rem { i } = ( N - i ) // K + 1 ;;
    if (( K % var 2 == 0 )) {
        count += ( rem { 0 } * ( rem { 0 } - 1 ) ) // 2 ;;
        for i in range ( 1 , K // 2 ) :
            count += rem { i } * rem { K - i } ;;
        count += ( rem { K // 2 } * ( rem { K // 2 } - 1 ) ) // 2 ;;
    }
     else{
        count += ( rem { 0 } * ( rem { 0 } - 1 ) ) // 2 ;;
        for i in rage ( 1 , K // 2 + 1 ) :
            count += rem { i } * rem { K - i } ;;
    }
    return count ;;
}
if (var __name__ == "__main__") {
    var N = 10 ; K = 4 ;;
    System.out.println ( findPairCount ( N , K ) ) ;;
}
 